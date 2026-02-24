# Bit flag positions (0-7)

IS_ADMIN = 1 << 7

CAN_DELETE = 1 << 6

CAN_WRITE = 1 << 5

CAN_READ = 1 << 4

IS_BANNED = 1 << 3

IS_VERIFIED = 1 << 2

HAS_PAID = 1 << 1

IS_ONLINE = 1 << 0

print(IS_ADMIN, CAN_DELETE, CAN_WRITE, CAN_READ, IS_BANNED, IS_VERIFIED, HAS_PAID, IS_ONLINE)

user = CAN_READ | IS_ONLINE | IS_VERIFIED # 0b00010101

print(user)


# CHECK flag

print("Can read?", bool(user & CAN_READ))


# SET a flag

user |= CAN_WRITE # turn on write

print(bin(user))


# CLEAR a flag (AND with NOT mask)

user &= ~IS_ONLINE

print(bin(user))


# TOGGLE a flag

user ^= HAS_PAID

print(bin(user))