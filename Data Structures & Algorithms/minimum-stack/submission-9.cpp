class MinStack {
public:


    MinStack() {
        
    }
    
    void push(int val) {
        minStack.push_back(val);
        if (val<=getMin()){
            min.push_back(val);
        }
    }
    
    void pop() {
        if (getMin() == top()){
            min.pop_back();

        }minStack.pop_back();
        
    }
    
    int top() {
        return minStack.back();
    }
    
    int getMin() {
        return min.back();
    }
private:
    std::vector<int> min = {INT_MAX};
    std::vector<int> minStack;
};
