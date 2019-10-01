
'''
쿠키 박스가 5, 10, 20개 짜리가 있고,
    사용자가 주문한 것을 최적의 쿠키 박스에 담아서 줘야 합니다.

- one type of cookie
- box 3 types
- user order with number
  -> more than 20, multiple boxes
    -> box 개수 최소화 -> 
    -> 2 small > 1 big box
    
    
order: number -> list of box
box: 
    - type
	- price
    - number_of_cookie : int
    
    
        
[box] get_boxes(주문량)

input: 주문량
output: [box]


'''    
class BoxType(Enum):
    SMALL = 5
    MEDIUM = 10
    LARGE = 20

class Box:
    type
    price
    number_of_cookie # number that actually inserted
    

class BoxPackSystem:
    boxes = dict() # key: BoxType, val: list of boxes
  
    def insert_new_box(self, box):
        if box.type not in boxes:
            self.boxes[box.type] = list()
        self.boxes[box.type].append(box)
        
    def get_box(self, type):
        if type.value not in boxes:
            return None
        return boxes[type.value].pop()
        
        
    def get_boxes(self, number) -> list:
        box_list = []
        for type in reversed(BoxType):
            while number >= type.value and type.value in boxes:
                box = self.get_box(type)
                if not box:
                    break
                box_list.append(box)
                number -= type.value
                               
        # number >= 0
                
        # no box left or small number than small box type
        if number == 0:
            return box_list
        
        for type in BoxType:
            if number <= type.value:
	            box = self.get_box(type)
            	box_list.append(box)
        		return box_list
            
        raise Exception

    
class RichBoxPackSystem(BoxPackSystem):

    def get_boxes(self, number) -> list:




