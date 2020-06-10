package it.sample.jpa.model;

import java.io.InputStreamReader;
import java.sql.Connection;
import java.sql.Statement;
import java.util.HashMap;
import java.util.Map;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import javax.sql.DataSource;

import org.dbunit.IDatabaseTester;
import org.dbunit.JdbcDatabaseTester;
import org.dbunit.database.IDatabaseConnection;
import org.dbunit.dataset.DataSetException;
import org.dbunit.dataset.IDataSet;
import org.dbunit.dataset.ITable;
import org.dbunit.dataset.ReplacementDataSet;
import org.dbunit.dataset.xml.FlatXmlDataSet;
import org.dbunit.dataset.xml.FlatXmlDataSetBuilder;
import org.dbunit.operation.DatabaseOperation;
import org.eclipse.persistence.config.PersistenceUnitProperties;
import org.h2.jdbcx.JdbcDataSource;
import org.h2.tools.RunScript;
import org.junit.rules.ExternalResource;

public class JpaTestRule extends ExternalResource {
	private static Connection connection;
	private static EntityManagerFactory entityManagerFactory;
	private IDatabaseTester databaseTester;
	private static String URLDb = "jdbc:h2:mem:~/test;";

	private static EntityManager entityManager;
	protected static final String SQL_SCHEME_SCRIPT_PATH = "sql/createDB_persistence.sql";
	
	@Override
	public void before() throws Exception {
		DataSource ds = createDataSource();
		Map<String, DataSource> properties = new HashMap<String, DataSource>();

		properties.put(PersistenceUnitProperties.NON_JTA_DATASOURCE, ds);

		entityManagerFactory = Persistence.createEntityManagerFactory("JpaSamplePersistence", properties);
		entityManager = entityManagerFactory.createEntityManager();
		
		connection = ds.getConnection();
		RunScript.execute(connection,
				new InputStreamReader(ClassLoader.getSystemResourceAsStream(SQL_SCHEME_SCRIPT_PATH)));
		
		databaseTester = new JdbcDatabaseTester("org.h2.Driver", URLDb, "sa", "");
	}

	@Override
	public void after() {
		try {
			Statement statement = connection.createStatement();
			statement.execute("DROP ALL OBJECTS");
			statement.close();
			connection.close();
		} catch(Exception e) {
			throw new RuntimeException(e);
		}
	}
	
	public void initData(String dataSetPath) throws Exception {
		IDataSet dataSet = getDataSetFromFile(dataSetPath);
		IDatabaseConnection iConn = databaseTester.getConnection();
		DatabaseOperation.CLEAN_INSERT.execute(iConn, dataSet);
	}

	public DataSource createDataSource() {
		JdbcDataSource ds = new JdbcDataSource();
		ds.setURL(URLDb);
		ds.setUser("sa");
		ds.setPassword("");
		return (DataSource) ds;
	}

	public void commitObj(Object obj) {
		entityManager.getTransaction().begin();
		entityManager.persist(obj);
		entityManager.getTransaction().commit();
	}
	
	public void assertTableContent(String tableName, String expectedDataset) throws Exception {
		ITable expected = getTableFromFile(tableName, expectedDataset);
		ITable actual = getTableFromDb(tableName);
		org.dbunit.Assertion.assertEquals(expected, actual);
	}
	
	private ITable getTableFromFile(String tableName, String dataSetPath) throws Exception {
		IDataSet dataSet = getDataSetFromFile(dataSetPath);
		return dataSet.getTable(tableName);
	}

	private IDataSet getDataSetFromFile(String dataSetPath) throws DataSetException {
		FlatXmlDataSet flatXMLDataSet = new FlatXmlDataSetBuilder().setColumnSensing(false).build(ClassLoader.getSystemResourceAsStream((dataSetPath)));
		ReplacementDataSet dataSet = new ReplacementDataSet(flatXMLDataSet);
		dataSet.addReplacementObject("[null]", null);
		flatXMLDataSet.endDataSet();
		return dataSet;
	}
	
	private ITable getTableFromDb(String tableName) throws Exception{
		IDatabaseConnection iDatabaseConnection = databaseTester.getConnection();
		IDataSet actual_data_set = iDatabaseConnection.createDataSet();
		ITable actual_table = actual_data_set.getTable(tableName);
		iDatabaseConnection.close();
		return actual_table;
	}
}
