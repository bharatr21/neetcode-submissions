class Shape {
public:
    virtual ~Shape() {}
    virtual Shape* clone() const = 0;
};

class Rectangle : public Shape {
private:
    int width;
    int height;

public:
    Rectangle(int w, int h) : width(w), height(h) {}

    int getWidth() const {
        return width;
    }

    int getHeight() const {
        return height;
    }

    Shape* clone() const override {
        Rectangle* rect = new Rectangle(this->getWidth(), this->getHeight());
        return rect;
    }
};

class Square : public Shape {
private:
    int length;

public:
    Square(int l) : length(l) {}

    int getLength() const {
        return length;
    }

    Shape* clone() const override {
        Square* sqr = new Square(this->getLength());
        return sqr;
    }
};

class Test {
public:
    vector<Shape*> cloneShapes(const vector<Shape*>& shapes) {
        vector<Shape*> newShapes;
        for(Shape* shape: shapes) {
            newShapes.push_back(shape->clone());
        }
        return newShapes;
    }
};
