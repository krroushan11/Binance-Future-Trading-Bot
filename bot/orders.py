import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"REQUEST: {symbol} {side} {order_type} qty={quantity} price={price}")

        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        else:
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(f"RESPONSE: {response}")

        return {
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice", "N/A")
        }

    except Exception as e:
        logging.error(f"ERROR: {str(e)}")
        return {"error": str(e)}