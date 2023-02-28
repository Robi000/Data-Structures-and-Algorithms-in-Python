"""
A class serves as the primary means for abstraction in 
object-oriented programming.

A class provides a set of behaviors in the form of member
functions (also known as methods), with implementations 
that are common to all instances of that class.


"""
#!-----------------------------------------------------------------
#!-----------------------------------------------------------------
#!-----------------------------------------------------------------

# * ----- Basics ------------

# class CreditCard:
#     def __init__(self, customer, bank, acnt, limit) -> None:
#         """create new credit card instance

#         Args:
#             customer (str): name of customer
#             bank (str): name of the bank
#             acnt (int ): account idetnetifiewr
#             limit (int): card limit
#         """
#         self._customer = customer
#         self._bank = bank
#         self._account = acnt
#         self._limit = limit
#         self._balance = 0

#     def get_customer(self):
#         """return name of the customer"""
#         return self._customer

#     def get_bank(self):
#         """return banks name"""
#         return self._bank
#     def get_account(self):
#         """Return the card identifying the number
#         """
#         return self._account
#     def get_limit(self):
#         """return the current credit limit
#         """
#         return self._limit
#     def get_balance(self)
#         """return current balance"""
#         return self._balance
#     def charge(self,price):
#         """ charge given price to card"""
#         if price + self._balance > self._limit:
#             return False
#         else:
#             self._balance += price
#             return True
#     def make_payment(self, amount):
#         self._balance -= amount


# class Vector:
#     """ecample class
#     """

#     def __init__(self, n):
#         """return n long 0 array

#         Args:
#             n (int ): number of element

#         Returns:
#             list : 0 arry
#         """
#         self._coords = [0] * n

#     def __len__(self):
#         return len(self._coords)

#     def __getitem__(self, j):
#         """normally return when self[] called

#         Args:
#             j (index):

#         Returns:
#             element : x
#         """
#         return self._coords[j]

#     def __setitem__(self, j, val):
#         """set value of self[j]

#         Args:
#             j (int):  index
#             val (element ): any type
#         """
#         self._coords[j] = val

#     def __add__(self, other):
#         x = min(len(self), len(other))

#         j = 0
#         result = [0] * x
#         while j < x:
#             result[j] = self._coords[j] + other._coords[j]
#             j += 1

#         result += self._coords[j:] + other._coords[j:]


# # how range class is working
# class Range:
#     def __init__(self, start, stop=None, step=1) -> None:
#         """initalize range

#         Args:
#             start (int): int
#             stop (int , optional): int . Defaults to None.
#             step (int , optional): int . Defaults to 1.

#         """

#         if step == 0:
#             raise ValueError("step cant be 0")

#         if stop == None:
#             start, stop = 0, start

#         # length

#         self._length = max(0, (stop - start + step - 1) // step)
#         self._start = start
#         self._step = step

#     def __len__(self):
#         """
#         return length of range
#         """

#         return self._length

#     def __getitem__(self, k):
#         """reutrn at index k(using standard interpretation)

#         Args:
#             k (int ): index
#         """

#         if k < 0:
#             k += len(self)

#         if not 0 <= k < self._length:
#             raise IndexError("index out of range")

#         return self._start + k * self._step


#!-----------------------------------------------------------------
#!-----------------------------------------------------------------
#!-----------------------------------------------------------------

# * ----- Hierarchy of Numeric Progression ------------

"""
A numeric progression is a sequence of numbers,
where each number depends on one or more of the previous numbers.

progression
requires a first value, and a way of identifying a new value based on one or more
previous values
"""


class Progression:
    """ this is a generic progression 
    """

    def __init__(self, start=0) -> None:
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopAsyncIteration
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(" ".join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):
    def __init__(self, start=0, increment=1) -> None:
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment


class GeometricProgression(Progression):
    def __init__(self, start=0, base=2) -> None:
        super().__init__(start)
        self._base = base

    def _advance(self):

        self._current *= self._base


class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1) -> None:
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current


start = FibonacciProgression()

print(next(start))
print(next(start))
print(next(start))
print(next(start))
print(next(start))


if __name__ == "__main__":
    print("Default progression:")
    Progression().print_progression(10)
    print("Arithmetic progression with increment 5:")
    ArithmeticProgression(5).print_progression(10)
    print("Arithmetic progression with increment 5 and start 2:")
    ArithmeticProgression(5, 2).print_progression(10)
    print("Geometric progression with default base:")
    GeometricProgression().print_progression(10)
    print("Geometric progression with base 3: ")
    GeometricProgression(3).print_progression(10)
    print("Fibonacci progression with default start values:")
    FibonacciProgression().print_progression(10)
    print("Fibonacci progression with start values 4 and 6:")
    FibonacciProgression(4, 6).print_progression(10)
