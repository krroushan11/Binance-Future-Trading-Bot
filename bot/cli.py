import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="🚀 Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", required=False, help="Required for LIMIT")

    args = parser.parse_args()

    try:
        validate_order(args.symbol, args.side, args.type, args.quantity, args.price)

        client = get_client()

        result = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n========== ORDER SUMMARY ==========")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")
        print(f"Price    : {args.price}")

        print("\n========== RESPONSE ==========")

        if "error" in result:
            print(f"❌ ERROR: {result['error']}")
        else:
            print("✅ Order Successful!")
            print(f"Order ID     : {result['orderId']}")
            print(f"Status       : {result['status']}")
            print(f"Executed Qty : {result['executedQty']}")
            print(f"Avg Price    : {result['avgPrice']}")

    except Exception as e:
        print(f"❌ VALIDATION ERROR: {str(e)}")


if __name__ == "__main__":
    main()