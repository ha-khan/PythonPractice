import asyncio

class PrintAlternatively:
    def __init__(self, left:str, right: str, n: int):
        self.n = n
        self.left, self.left_count = left, 0
        self.right, self.right_count = right, 0

        self.buffer = ""
    
    async def buffer_left(self):
        if self.left_count == self.n:
            return
        
        self.left_count += 1
        self.buffer += self.left

        await self.buffer_right()

    async def buffer_right(self):
        if self.right_count == self.n:
            return
        
        self.right_count += 1
        self.buffer += self.right

        await self.buffer_left()
    
    def __repr__(self) -> str:
        return self.buffer
        

def main():
    c = PrintAlternatively("foo", "bar", 2)
    asyncio.run(c.buffer_left())
    print(c)


if __name__ == '__main__':
    main()