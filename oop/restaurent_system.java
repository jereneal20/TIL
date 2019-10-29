


interface IBooker {
    private List<IRequest> bookRequests;
    
    void request(LocalDateTime startTime, LocalTimeTime endTIme, int people);
    void notifyBookRequestResult(IRequest req)
}

interface IRequest {
    private int people;
    private IBooker booker;
    private LocalDateTime startTime;
    private LocalDateTIme endTime;
    private ITable table;
    LocalDateTime getTime();
    // getUser
}

interface IRestaurant {
    private List<ITable> tables;
    private Map<ILocalDate, List<IRequest>> bookRequests;
    private Map<ILocalDate, List<IRequest>> confirmBooking;
    private List<ITableBookingPolicy> policy; 

    boolean requestBook(IRequest req);
    void getTableStatus(LocalDateTime time);
    List<IRequest> getBookRequests();
    void confirmRequest(IRequest req);
    void denyRequest(IRequest req);
}

interface ITable {
    private int capcity;

    boolean status();
    void setStatus(boolean status);
    int getCapacity();
}

interface IManager {
    List<IRequest> showBookingStatus(LocalDateTime);
    List<IRequest> showBookRequests(LocalDateTime);
    void confirmRequest(IRequest req);
    // notify...
}

class NoodleRestaurant implements IRestaurant {
	public boolean requestBook(IRequest req) {
        List<IRequest> bookAtTime = new ArrayList<>();
        
        for (booking : confirmBooking) {
            if (book.startTime().after(req.getTime()) && book.endTime().before(req.getTime())) {
                bookAtTime.add(book);
            }
        }

        List<Table> emptyTables = new ArrayList<>();
        emptyTables.addAll(restaurant.getTables());
        for (booking book : bookAtTime) {
            emptyTables.remove(book.getTable());
        }
        
        List<ITable> availableTables = new ArrayList<>();
        for (ITable table : emptyTables) {
            if (table.capacity >= req.people) {
                availableTables.add(ITable);
            }
        }
        
        if (!availableTables.isEmpty()) {
			bookRequests.add(req);
            return true;
        } else {
            return false;
        }
    }

    public void confirmRequest(IRequest req) {
    	confrimBooking.add(req);
        requ.getBooker().notifyBookRequestResult(req);
    }
}







