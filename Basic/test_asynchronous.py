import asyncio

async def check_endpoint(name, delay):
    await asyncio.sleep(delay)
    return f"{name}: healthy"

async def run_health_checks():
    results = await asyncio.gather(
        check_endpoint("auth-service", 0.2),
        check_endpoint("orders-service", 0.1),
        check_endpoint("search-service", 0.3),
    )
    for r in results:
        print(r)

asyncio.run(run_health_checks())