#ifndef BOARDGAME_H
#define BOARDGAME_H

#include <string>

using namespace std;

class BoardGame {
public:
    virtual int rows() = 0;
    virtual int cols() = 0;
    virtual string get_val(int x, int y) = 0;
    virtual void play_at(int x, int y) = 0;
    virtual bool finished() = 0;
    virtual string message() = 0;
};


#endif // BOARDGAME_H