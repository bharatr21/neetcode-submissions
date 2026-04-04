class Meal {
private:
    double cost;
    bool takeOut;
    string main;
    string drink;

public:
    double getCost() {
        return cost;
    }

    bool getTakeOut() {
        return takeOut;
    }

    string getMain() {
        return main;
    }

    string getDrink() {
        return drink;
    }

    void setCost(double cost) {
        this->cost = cost;
    }

    void setTakeOut(bool takeOut) {
        this->takeOut = takeOut;
    }

    void setMain(string main) {
        this->main = main;
    }

    void setDrink(string drink) {
        this->drink = drink;
    }
};

class MealBuilder {
public:
    Meal* meal;
    MealBuilder() {
        meal = new Meal();
    }

    MealBuilder& addCost(double cost) {
        this->meal->setCost(this->meal->getCost() + cost);
        return *this;
    }

    MealBuilder& addTakeOut(bool takeOut) {
        this->meal->setTakeOut(takeOut);
        return *this;
    }

    MealBuilder& addMainCourse(string main) {
        this->meal->setMain(main);
        return *this;
    }

    MealBuilder& addDrink(string drink) {
        this->meal->setDrink(drink);
        return *this;
    }

    Meal build() {
        return *(this->meal);
    }
};
