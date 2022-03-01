"""
The same instance of FooBar will be passed to two different threads.
Thread A will call foo() while thread B will call bar().
Modify the given program to output "foobar" n times.

Example 1:
Input: n = 1
Output: "foobar"
Explanation: 
    There are two threads being fired asynchronously. 
    One of them calls foo(), while the other calls bar(). "foobar" is being output 1 time.

Example 2:
Input: n = 2
Output: "foobarfoobar"
Explanation: "foobar" is being output 2 times.
"""
import threading

class FooBar:
    def __init__(self, n: int):
        self.n = n
        self.foo_mutex = threading.Lock()
        self.bar_mutex = threading.Lock()
        self.buffer = ""

        self.bar_mutex.acquire()
    
    def foo(self):
        for _ in range(self.n):
            self.foo_mutex.acquire()
            self.buffer += "foo" 
            self.bar_mutex.release()
    
    def bar(self):
        for _ in range(self.n):
            self.bar_mutex.acquire()
            self.buffer += "bar" 
            self.foo_mutex.release()
    
    def __repr__(self) -> str:
        return self.buffer

def main():
    f = FooBar(5)
    t1 = threading.Thread(target=f.foo)
    t2 = threading.Thread(target=f.bar)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f)

if __name__ == '__main__':
    main()