clear; clc;
%perhitungan panjang gelombang dan tebal rambut
disp('Panjang Gelombang Laser dan Tebal Rambut')
disp('-------------------------------------------')
v=input('masukkan panjang gelombang laser :')
w=input('masukkan orde ke-n: ');
x=input('masukkan konstanta kisi: ');
y=input('masukkan rata-rata jarak orde-n ke terang pusat: ');
z=input('masukkan jarak kisi-layar: ');
lambda = (1/(x*w))*(y/sqrt((z)^2+(y)^2));
Drambut = (v*w*z)/y;
fprintf('Besar Panjang Gel. Laser = %.4f\n',lambda)
fprintf('Besar Diameter Rambut = %.4f\n',Drambut)

%Data Difraksi Celah Tunggal dan Celah Ganda
datasudut=1:80;
dataIntenA1=[0.9671 0.8735 0.7338 0.5686 0.4007 0.2504 0.1323 0.0529 0.0113 0 0.0081 0.0242 0.039 0.0466 0.0454 0.0369 0.0247 0.0127 0.004 0.0002 0.0011 0.0051 0.0102 0.0144 0.0164 0.0157 0.0128 0.0087 0.0046 0.0015 0.0001 0.0003 0.0019 0.0041 0.0063 0.0078 0.0083 0.0078 0.0065 0.0046 0.0012 0.0003 0.0003 0 0.0004 0.0012 0.0023 0.0034 0.0043 0.0049 0.005 0.0048 0.0042 0.0035 0.0026 0.0018 0.001 0.0005 0.0001 0 0.0001 0.0003 0.0007 0.0011 0.0016 0.0021 0.0025 0.0028 0.0031 0.0032 0.0033 0.0034 0.0033 0.0032 0.0031 0.0029 0.0028 0.0026 0.0024 0.0022];
dataIntenA2=[0.9809	0.9255	0.8387	0.7283	0.6037	0.475	0.3517	0.2417	0.1507	0.0818	0.0354	0.0094	0.0002	0.0031	0.0131	0.0255	0.0368	0.0444	0.0472	0.0452	0.0392	0.0308	0.0215	0.0128	0.006	0.0017	0	0.0007	0.0032	0.0067	0.0103	0.0135	0.0156	0.0165	0.016	0.0145	0.0121	0.0093	0.0064	0.0038	0.0018	0.0006	0	0.0002	0.0009	0.0021	0.0035	0.0049	0.0062	0.0073	0.008	0.0083	0.0083	0.0079	0.0073	0.0065	0.0055	0.0045	0.0035	0.0026	0.0018	0.0011	0.0006	0.0003	0.0001	0	0.0001	0.0002	0.0005	0.0008	0.0011	0.0004	0.0018	0.0021	0.0025	0.0028	0.0031	0.0033	0.0036	0.0038];
dataIntenB1=[0.903 0.65	0.34 0.091	0 0.101	0.355 0.663	0.909 1.000	0.903	0.656	0.352	0.104	0	0.078	0.307	0.602	0.861	0.993	0.956	0.765	0.487	0.216	0.307	0.008	0.134	0.371	0.645	0.874	0.992	0.968	0.813	0.575	0.319	0.113	0.008	0.026	0.159	0.371	0.609	0.82	0.958	0.999	0.939	0.794	0.596	0.384	0.916	0.063	0.003	0.021	0.11	0.252	0.425	0.603	0.764	0.89	0.971	1.000	0.979	0.915	0.818	0.698	0.567	0.436	0.314	0.208	0.123	0.06	0.02	0.002	0.003	0.021	0.051	0.092	0.138	0.189	0.241	0.292];
dataIntenB2=[0.94 0.79 0.565 0.329 0.132 0.017 0.011 0.114	0.302 0.533	0.756 0.923	0.998 0.965	0.834 0.633	0.405 0.198	0.053 0	0.047 0.183	0.379 0.598	0.796 0.938	0.999 0.969	0.857 0.685	0.482 0.286	0.124 0.025	0.001 0.053	0.171 0.335	0.519 0.699	0.85 0.953 0.998 0.982 0.91	0.793 0.645 0.485 0.33	0.194 0.089	0.023 0	0.018 0.074	0.16 0.267	0.388 0.513	0.633 0.742	0.835 0.909	0.961 0.991	1.000 0.99	0.964 0.924	0.874 0.816	0.754 0.689	0.625 0.562	0.502 0.446	0.394 0.348	0.307];

%Grafik percobaan Difraksi Celah Tunggal
plot(datasudut,dataIntenA1,'b-*',datasudut,dataIntenA2,'r-*');
    title('hubungan intensitas relatif dengan sudut difraksi dan interferensi celah tunggal')
    xlabel('sudut'),ylabel('intensitas relatif')
    legend('panjang gelombang 520 nm','panjang gelombang 685 nm')
  grid on
%Grafik percobaan Difraksi dan Interferensi Celah Ganda
figure;
plot(datasudut,dataIntenB1,'b*-',datasudut,dataIntenB2,'r*-')
    title('hubungan intensitas relatif dengan sudut difraksi dan interferensi celah ganda')
    xlabel('sudut'),ylabel('intensitas relatif')
    legend('panjang gelombang 520 nm','panjang gelombang 685 nm')
  grid on