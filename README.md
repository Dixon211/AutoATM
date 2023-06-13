![image](https://github.com/Dixon211/AutoATM/assets/131546168/e3b257e1-badd-4a5d-a21e-f2b3d7a58b20)  
# AutoATM
## Robots Making Money for You!

### Development   
- Open 2 terminals (or split vscode terminal)
- in one, run `cd frontend && npm start`
- in the other, run `cd backend && python app.py`
- Appreciate RH #1 stock chart

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
	

Changes 6/12--------------------------------------------------------------------
GUI/Testing:
	Currently Added:
		Matlab plot to show sell floor visualization (so helpful)

	Want to Add:
		EoD Report: Send an Eod report after all stocks are sold showing net profit/loss for the day then sends it in an email. Would allow for testing algorithm before spending real money.

		Detailed Eod report: Long Term, EoD report but could also show stocks traded and value from each. Could possibly also feed this to an LLM in future?

Algorithms:
	Currently completed:
		-Sell Floor with Low Pass Filter:
			 Location: Stock class, runfilter() method
			
			from information from Robinhood creates a SELL FLOOR that will update when the price of the stock goes up, and when stock drops will sell. Low Pass Filter adds data smoothing to help with delay. (Thank you Julian)

		-Sell Floor Buffer:
			Location: Stock class, buy() method
		
			Part of the Sell Floor that allows for a 5% loss before selling and keeps he sell floor 5% below current buy price

	Need to check:
		Sell Floor Initilization: Sell Floor initialized as 0 and so the first change as the data would come in would add a strong weight to sell the stock almost instantly resulting in majority loses. Need to confirm that this intializes as a None value. Need to check if setting up an initialization sequence could help to do 3 pulls, create sell floor on this information, activate the use of buy/sell functions

	Need to Add:
		-Sell Floor Buffer variable Threshold: Possible to add something like a Buffer % threshold so if a stock worth $300 is bought we can't potentially lose $15/share if it instantly drops. Possibly just set acceptable loss % so something like
			if buyprice < 25.00
				floor buffer = 95%
			if buyprice >= 25.00
				floor buffer = 96%
			if buyprice>= 100.00
				floor buffer = 98%
			if buyprice = $300.00
				floor buffer = 99%
		
		-Time of Execution: when program should resume trading at the beginning of the day and stop at the end, allow a buffer from start of day by 30mins and end of day by 30 minutes to migate edge cases.

		-EoD Sell: Sell all stocks at EoD to avoid swings in market at off hours

		-Sell when stock drops below top 50/100/whatever: Set event for if the stock is in dixonstocks but is not in the new stock dictionary then sell the stock as it is assumed to be below the sell threshold, but the program cannot update the info. Possibly add a default Sell() on any stock update error

		-Multiple Stock Buy: Don't have anything concrete yet, but need to add a way to pull the current usable $ value in the Robinhood account, then choose to buy multiple stocks if there is money for it, but needs to be able to not spend it all on the first stock, simple solution could be adding a stock limit like 5 of the same stock is max so it will move on. I would rather buy a variety than pray for a single stock to go up as we would have less chance of a blowout, long story short; diversify your portfolio!

Data exploration:
	Currently added:
		Top 100 Pull (Robinhood):
			Location: Parent, search: rs.get_top_100()
			Pulls the top 100 and add the data to a dictionary

	Need to Add:
		Pull Available Funds (Robinhood):
			Need to pull available funds from the target account and store. For testing set as a set value

	Want to Add:
		LLM interaction:
			using an up to date database LLM, possibly Phinder, at beginning of day have it send a prompt with parameters like
				-You are a renowned Financial Analyst
				-I am your client
				-recommend me a list of the 100 best stocks to buy
				-put that list in (key, value pair) in JSON format
			then have the app pull the JSON information and buy those instead of generic top 100

API Interactions:
	Currently Done:
		API Credentials (Robinhood): stored API credentials as a local file that are not uploaded to Github and allow to view information through my account.

	Need to Add:
		API Buy/Sell (Robinhood):
			After algorithm is completed and tested, allow program to make trades using Robinhood.
			

