package it.sample.java;

import java.util.concurrent.BlockingQueue;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.LinkedBlockingDeque;

public class KeyBasedExecutor {

	private static final int QUEUE_ARRAY_SIZE = 5;
	public static final KeyBasedExecutor INSTANCE = new KeyBasedExecutor();
	
	private BlockingQueue<Runnable>[] queues = new BlockingQueue[QUEUE_ARRAY_SIZE];
	private Future<?>[] runnings = new Future[QUEUE_ARRAY_SIZE];
	protected ExecutorService executorService;
	
	private KeyBasedExecutor() {
		executorService = Executors.newFixedThreadPool(QUEUE_ARRAY_SIZE);
		for (int i=0; i<QUEUE_ARRAY_SIZE; i++) {
			queues[i] = new LinkedBlockingDeque<>();
		}
	}
	
	//Viene assicurato ordine di esecuzione dei task che vengono inseriti nella stessa BlockingQueue
	public void submit(Object key, Runnable task) {
		int idx = key.hashCode() % QUEUE_ARRAY_SIZE; //logica di partizione per definire la blockingQueue sulla quale inserire il task
		queues[idx].offer(task);
		ensureRunning(idx);
	}

	private synchronized void ensureRunning(int idx) {
		if (runnings[idx] == null || runnings[idx].isDone()) {
			runnings[idx] = executorService.submit(() -> execute(idx));
		}
	}
	
	private void execute(int idx) {
		try {
			while(true) {
				queues[idx].take().run();
			}
		} catch(Exception e) {
			throw new RuntimeException(e);
		}
	}
}
