package it.sample.java;

import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.function.Consumer;

import org.junit.Test;

public class MockSynchronizedActionTest {

	private void testConcurrent(Consumer<Integer> test, int numThreads) throws Exception {
        CountDownLatch latch = new CountDownLatch(1);
        ExecutorService service = Executors.newFixedThreadPool(numThreads);
        Collection<Future<Integer>> futures = new ArrayList<>(numThreads);
        
        for (int t = 0; t < numThreads; t++) {
            final int i = t;
            futures.add(
                service.submit(() -> {
                    try {
                        latch.await();
                        test.accept(i);
                    } catch (Exception e) {
                        throw new RuntimeException(e);
                    }
                    return i;
                }));
        }
        
        latch.countDown();
        for (Future<Integer> f : futures) {
            f.get();
        }
    }
    
    @Test
    public void testConcurrentSubscription() throws Exception {
        int numThreads = 10;
        
        testConcurrent(
                i -> {
                    
                    try {
                    	MockSynchronizedAction.INSTANCE.launchSynchronizedAction(i);
                    } catch (Exception e) {
                        throw new RuntimeException(e);
                    }
                },
                numThreads);
        
        assertEquals(10, MockSynchronizedAction.countInvocation);
        
        
    }
}
