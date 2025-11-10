class CoffeeMachine:

    def __init__(self, water, milk, beans, cups, cash):
        self.contents = {'water': water, 'milk': milk, 'beans': beans, 'cups': cups, 'cash': cash}
        
        
    def take_action(self, action):
        
        if action == 'buy':
            drink = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
            if drink == 'back':
                return

            # missing_ingredient will be equal to None if enough_content is False.
            enough_content, missing_ingredient = self.buy(int(drink))

            if enough_content:
                print('I have enough resources, making you a coffee!')
            else:
                print('Sorry, not enough {missing_ingredient}!')

        elif action == 'fill':
            self.fill()
        elif action == 'take':
            self.take()

        elif action == 'remaining':
            self.display_contents()
    
    
    def display_contents(self):
        print('''
The coffee machine has:
{water} of water
{milk} of milk
{beans} of coffee beans
{cups} of disposable cups
{cash} of money'''.format(**self.contents))
    
    
    def buy(self, drink_num: int) -> (bool, str):
        """
        deducts needed ingredients from the machine based on the drink number
        returns True if the machine has enough ingredients, False otherwise

        the return value is in the form of a tuple: (True/False, Missing ingredient/None)
        """
        # espresso: 250 ml of water and 16 g of coffee beans, $4.
        if drink_num == 1:
            needs = {'water': 250, 'milk': 0, 'beans': 16, 'cost': 4}

        # latte: 350 ml of water, 75 ml of milk, and 20 g of coffee beans, $7.
        elif drink_num == 2:
            needs = {'water': 350, 'milk': 75, 'beans': 20, 'cost': 7}

        # assuming user won't give any input other than 1, 2 or 3.
        # cappuccino: 200 ml of water, 100 ml of milk, and 12 g of coffee beans, $6.
        else:
            needs = {'water': 200, 'milk': 100, 'beans': 12, 'cost': 6}

        cost = needs.pop('cost')

        if self.contents['cups'] < 1:
            return False, None

        for key in needs.keys():
            if self.contents[key] < needs[key]:
                return False, key

        for key in needs.keys():
            self.contents[key] -= needs[key]

        self.contents['cups'] -= 1
        self.contents['cash'] += cost

        return True, None


    def fill(self):
        """
        asks user for amounts to deposit in the machine and adds it to the global
        machine dictionary.
        """
        ingredients = ['water', 'milk', 'beans', 'cups']
        for ing in ingredients:
            amount = int(input(f'{ing}: '))
            self.contents[ing] += amount
        
        
    def take(self):
        cash = self.contents['cash']
        self.contents['cash'] = 0
        print(f'I gave you {cash}$')
        
        

machine = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    action = input('\nWrite action (buy, fill, take) :\n')

    if action == 'exit':
        break
    machine.take_action(action)
