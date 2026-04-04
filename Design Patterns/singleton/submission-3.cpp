class Singleton {
private:
    string val;
    Singleton() {}
public:

    static Singleton *getInstance() {
        static Singleton instance;
        return &instance;
    }

    string getValue() {
        return val;
    }

    void setValue(string &value) {
        this->val = value;
    }
};
