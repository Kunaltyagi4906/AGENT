import asyncio
from livekit.agents import Agent

async def main():
    
    instructions = "You are a helpful AI voice agent. Answer user questions politely and clearly."

    agent = Agent(
        instructions=instructions,
        api_key="API5az8xGRCmqsa",
        api_secret="g5tRaijJWoLTQbEvvlDNi5oeRppXmLYUR6FAbmE1i4f",
        ws_url="wss://my-agent-5xteyuyz.livekit.cloud",
        room="test-room",
        identity="agent"
    )

    
    print("Agent connected and ready!")
    await agent.run_forever()

if __name__ == "__main__":
    asyncio.run(main())
