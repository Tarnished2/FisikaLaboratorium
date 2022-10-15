%perhitungan
disp('Perhitungan Waktu Paruh dan Konstanta Peluruhan Bahan')
t=input('Masukkan waktu yang telah berjalan : ');
N0=input('Masukkan jumlah nukleus pada waktu t : ');
tparuh = t/(log2(400/N0));
lambda = log(2)/tparuh;
fprintf('Besar Waktu Paro = %.3f\n',tparuh)
fprintf('Besar Konstanta Peluruhan = %.3f\n',lambda)

%plot grafik radioaktivitas
t=1:100;
y1=[379 357 340 316 297 278 262 242 225 214 198 186 173 166 156 147 141 134 129 119 112 108 98 96 89 88 83 77 74 71 68 64 61 58 54 51 49 44 42 39 37 34 33 32 29 28 28 27 25 23 21 21 19 17 16 15 15 13 13 12 12 11 10 10 9 9 9 9 8 8 7 7 6 5 5 5 5 4 4 4 3 3 3 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1]; %small
y2=[382 363 347 337 323 312 298 282 259 262 256 244 234 226 219 208 201 197 189 184 174 168 160 154 150 142 139 133 126 123 117 113 109 107 102 99 96 91 89 84 79 75 71 69 65 64 62 59 56 54 52 48 46 44 42 40 40 37 36 35 33 32 30 29 27 26 25 23 22 21 18 17 16 15 14 14 13 13 12 12 12 11 11 10 9 9 8 8 8 8 7 6 6 6 5 5 4 4 4 4]; %medium
y3=[394 384 375 369 361 357 349 339 333 327 317 311 304 300 292 287 281 274 267 266 261 253 244 242 236 231 226 222 216 212 208 202 198 193 189 186 181 175 172 168 165 162 157 155 150 146 145 141 139 137 133 129 128 125 121 119 117 116 114 111 109 108 105 103 101 99 97 95 93 91 88 86 85 82 82 80 79 78 76 75 74 72 71 70 69 68 66 65 64 62 60 60 58 57 56 55 55 54 52 51]; %large

plot(t,y1,'b--*',t,y2,'g--*',t,y3,'r--*');
    title('Grafik Percobaan Radioaktivitas')
    xlabel('waktu'),ylabel('jumlah nukleus')
    legend('small','medium','large')
  grid on

%plot grafik deteksi radiasi
r=0:10;
c=[291.7 235.4 174.1 152.3 115.7 111.1 85.2 67.8 62.7 53.9 45.8];
plot(r,c,'b--*');
    title('Grafik Percobaan Deteksi Radiasi')
    xlabel('jarak'),ylabel('cacahan rata2')

%plot grafik stern-gerlach
waktu=[15 30 45 60 75 90 105 120 135 150 165 180];
detatas=[19270 37467 55872 74126 93484 111867 130810 149564 168059 186801 205492 224346]; %detektor atas
detbawah=[19423 37516 55928 74046 93444 111693 130614 149378 167746 186532 205082 223997]; %detektor bawah
plot(waktu,detatas,'b--*',waktu,detbawah,'g--*');
    title('Grafik Percobaan Stern-Gerlach')
    xlabel('waktu'),ylabel('jumlah partikel')
    legend('partikel detektor atas','partikel detektor bawah')