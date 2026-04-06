class State {
public:
    virtual ~State() {}
    virtual void handleRequest(class Document* doc) = 0;
};

//Forward Declaration
class Draft: public State {
    void handleRequest(class Document* doc) override;
};
class Review: public State {
    void handleRequest(class Document* doc) override;
};
class Published: public State {
    void handleRequest(class Document* doc) override;
};

class Document {
private:
    State* state;
    bool approved;

public:
    Document() : approved(false), state(new Draft()) {}

    State* getState() const { return state; }

    void setState(State* newState) { delete state; state = newState; }

    void publish() { state->handleRequest(this); }

    void setApproval(bool approval) { approved = approval; }
    
    bool isApproved() const { return approved; }
};


void Draft::handleRequest(Document* doc) override {
    doc->setState(new Review());
}

void Review::handleRequest(Document* doc) override {
    if(doc->isApproved()) {
        doc->setState(new Published());
    } else {
        doc->setState(new Draft());
    }
}

void Publish::handleRequest(Document* doc) override {
}