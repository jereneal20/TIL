"""
Design restaurant system

"""

"""
- restaurant system
  -> search by person / make a reservation / cancellalation
    -> by person . number of people . date . time . -> phone number
     -> reservation time is 4 a day ?
     -> 
  -> tables . size
    -> table type (small, medium, large) -> 2, 4, 8

  -> 3 people -> 4 assign first, if not available in 4, then reserve on 8
  -> reservation wait (queue)
    -> if one of reservation is cancelled, then try to assign the first~ reservation

  -> reservation & table & time
    -> reservation time table -> date with 4 time -> number of tables by type -> rservation info is queued by table type
    -> small ? -> small table type available > number  0- > me -> lar   
    {datetime: {tabletype: [reservation....]}}
"""

class RestaurentReservationSystem:
    reserve_table = {datetime: [reservationInfo....]}
    reserve_count = {datetime: {tabletype, int}}

    waiting_table = {datetime: [reservationInfo....]}


    def make_a_reservation(rinfo):
        if (is_available(rinfo)):
            reserve_table[rinfo.datatime].append(rinfo)
            
    def is_availble(rinfo):
        for xxx in xxxxx:

class Table:
	type
    seats
    position
    id


class ReservationInfo:
    reserver_name
    number_of_people
    date
    time
    phone_number



"""
1차 시도
"""

"""

- 레스토랑 system
- reservation / cancel
  -> 예약자의 이름 / 날짜 / 시간: 2-hour / phone number
  -> table 당 예약 리스트
  -> 대기 예약 ( if any seats are available, then go to that seat)
  -> 4 times per day
  -> table assign by restauant
  -> 3 types of tables : 2, 4, 8
  -> no table merge
  -> 
  
- reservation 조회
- position & table number (number of seats)
"""

SMALL_TYPE = 1
MEDIUM_TYPE = 2
LARGE_TYPE = 3

import collections
collections.OrderedDict()

class Restaurant:
    table_type_list = defaultdict(list)
    def __init__():
	...
        
    def add_table(table):
    	self.table_type_list[table.type].appened(table)

	def reservation(reservationInfo) -> bool:
    	for type in range(SMALL_TYPE, LARGE_TYPE + 1):
        	for table in self.table_type_list[type]:
	        	table.available
		pass

class ReservationManager:
	
    
class Table:
    def __init__(...):
        self.position
    	self.id
	self.number_of_seats
	self.type
        self.reservation_infos = dict()
                 
	
class PersonalInfo:
    def __init__(name, pnumber):
    	pass
                 
class ReservationInfo:
    def __init__(pinfo, date, time):
	pass
