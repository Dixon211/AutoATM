GUI:
	1. 

Algorithms:
	1. Buy low sell high algorithm
		-allow window for no trading between first 30min and last 30 minutes of the trading day
		-needs to set what price the stock was bought at
		-needs to sell right before hitting this price
		-needs to sell 10% above what the stock was bought at (rough guess)
		-3 variables: buy price, stop loss price, profit price = buy price + 10%

Data exploration:
	1. Warren Buffet AI
		-Use OpenAI key to query Phind or another LLM to get suggested stocks to invest in
		-possible prompt:
			-Needs to find suggested stocks, would prefer it was Warren buffet
			-Have the prompt create a JSON file that the program can reference
			-Have the prompt name the JSON file the same thing everything
	2. Top 100 algorithm
		a. Down and dirty top 100 on robinhood no thought required
API interactions:
	1. Save API as a variable with protecting that is not pushed to github and can have local encryption

	1. Connecting to Robinhood API
		a. -Run the selected algorithm
		b. -Need to add rate limit to this to prevent being blocked or creating unwanted network issues.
		c. -Variable list: stock_name, stock_price, send to buy_high algorithm
		d. -Make a trade to target stock
		e. -How to sell stock in your portfolio
	
		
		
	

