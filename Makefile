all: backend/app/libgeo.so
backend/app/libgeo.so: cpp/geo.cpp
	g++ -std=c++20 -O3 -shared -fPIC cpp/geo.cpp -o $@
clean:
	rm -f backend/app/libgeo.so
