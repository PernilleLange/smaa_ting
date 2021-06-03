from math import ceil

class float_range:
    def __init__(self, *args):
        self.args = args
        if len(self.args) == 0 or len(self.args) > 3:
            raise TypeError
        elif len(self.args) == 1:
            self.start, self.stop, self.step = 0, self.args[0], 1
        elif len(args) == 2:
            self.start, self.stop, self.step = self.args[0], self.args[1], 1
        else:
            self.start, self.stop, self.step = self.args[0], self.args[1], self.args[2]

    def __iter__(self):
        new_start = self.start - self.step
        if self.stop > self.start and self.step > 0:
            bound = self.stop - self.step
            while new_start < bound:
                new_start += self.step
                yield new_start
        elif self.stop < self.start and self.step < 0:
            bound = self.stop + self.step * -1
            while new_start > bound:
                new_start += self.step
                yield new_start

    def __len__(self):
        length = ceil((self.stop - self.start) / self.step)
        if length < 0:
            return 0
        else:
            return length

    def __reversed__(self):


# #
# test = float_range(0.5, 7, 0.75)
# print([num for num in test.__iter__()])
# print([num for num in test.__reversed__()])
# test = float_range(1, 11, 2)
# print([num for num in test.__iter__()])
# print([num for num in test.__reversed__()])

# def float_range(*args):
#     if len(args) == 0 or len(args) > 3:
#          raise TypeError("Must be called with 1, 2, or 3 arguments.")
#     elif len(args) == 1:
#         start, stop, step = 0, args[0], 1
#     elif len(args) == 2:
#         start, stop, step = args[0], args[1], 1
#     else:
#         start, stop, step = args[0], args[1], args[2]
#     new_start = start - step
#     if stop > start and step > 0:
#         bound = stop - step
#         while new_start < bound:
#             new_start += step
#             yield new_start
#     elif stop < start and step < 0:
#         bound = stop + step * -1
#         while new_start > bound:
#             new_start += step
#             yield new_start

#
#
# print(len(float_range(1,5,1)))
#print([num for num in float_range(2,10,2,1,2)])





