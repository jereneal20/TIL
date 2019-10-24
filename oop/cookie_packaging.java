// 오늘 면접 준비 도와주면서 한 것.
// Requirement
// Cookie factory
// Packing size of boxes (small, medium, large)
// Box contains cokies
// factory : numbers -> boxes -> package
// package -> box -> cookies

// Storage (10, 50, 10)
// box contains cookies
// cookies
// Factory

// box > cookies
// Factory


// Box id
// Small box, large box (갯수)
// 명세 파악에 실패했다

interface IBoxStorage {
    Box makeSmallBox();
    Box makeMediumBox();
    Box makeLargeBox();
}

interface ICookie {
}

interface IBox {
    int size();
    int numOfCookies();
    List<Cookie> pop(int numOfCookies);
    void put(List<Cookie> cookies);
}

interface ICookieFactory {
    List<Box> makeCookieBox(int cookies)
}

// Impl
class ChocoCookie implements ICookie {
}

class SmallBox implements IBox {
    private List<Cookie> cookies = new ArrayList<Cookie>();
    private static final size = 10;
    public SmallBox(List<Cookie> cookies) {
        cookies.addAll(cookies);
    }
    public int size() {
        return this.size;
    }
    public int numOfCookies() {
        return cookies.size();
    }
    public List<Cookie> pop(int numOfCookies) {}
    public boolean put(List<Cookie> cookies) {
    }
}

class MediumBox implements IBox {
}

class LargeBox implements IBox {
}

enum BoxInformation {
    Large(10), Medium(200), Small(300);
}

class CookieFactory implements ICookieFactory {
    public CookieFactory(IBoxStorage storage) {
        this.boxStorage = storage;
    }
    
    private IBoxStorage boxStorage;
    public List<Box> makeCookieBox(int cookies) {
      	while (cookies > 0) {
            boxStorage.
        }
    }
}

class BoxStorage implements IBoxStorage {
    private int small;
    private int medium;
    private int large;
    
    public BoxStorage(small, medium, large) {
    }
    
    public Box makeSmallBox() {
    }
    public Box makeMediumBox() {
    }
    public Box makeLargeBox() {
    }
}

