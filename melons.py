"""This file should have our order classes in it."""
import random

class AbstractMelonOrder(object):

    def __init__(self, species, qty, order_type, tax, flat_fee = 0):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        self.inspected = False

    def get_base_price(self):
        self.base_price = random.randint(5,9)

        return self.base_price

    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()

        if self.species == "christmas":
            base_price = 1.5 * base_price
            
        total = ((1 + self.tax) * self.qty * base_price)
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def passed_inspection(self):
        """Set shipped to true."""

        self.inspected = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""
    #We are calling the parent classes dunder intial method
    #to intialize attributes: species and quantity
    #Then we call this classes dunder init method to intialize
    #attributes: order_type and tax
    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    #We are calling the parent classes dunder intial method
    #to intialize attributes: species and quantity
    #Then we call this classes dunder init method to intialize
    #attributes: order_type and tax and country code
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)
        self.country_code = country_code

    def get_total(self):
        """Calculate price."""
        
        if self.qty < 10:    
            total = super(InternationalMelonOrder, self).get_total() + 3
        else: 
            total = super(InternationalMelonOrder, self).get_total()

        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """GovernmentMelonOrder with no tax"""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(GovernmentMelonOrder, self).__init__(species, qty, "government", 0.00)
