package it.sample.java;

public class MockSynchronizedAction {

	public static MockSynchronizedAction INSTANCE = new MockSynchronizedAction();
	
	public static int countInvocation = 0;
	
	private MockSynchronizedAction() {
		
	}
	
	public void launchSynchronizedAction(int i) {
		System.out.println("Running Thread " + Thread.currentThread().getName() + "by iteration " + i);
		countInvocation++;
	}
	
}
