#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

//20-07-15(수) 시작
#if 0 // A-B

#include <stdio.h>

int main(void) {
	int inpt1, inpt2;

	scanf("%d %d", &inpt1, &inpt2);
	printf("%d", inpt1 - inpt2);

	return 0;
}




#elif 0 // 엄청난 부자2 (플레문제) 파이썬으로 품

#include <stdio.h>

int main(void) {
	int inpt1, inpt2;

	scanf("%d %d", &inpt1, &inpt2);
	printf("%d\n", inpt1 / inpt2);
	printf("%d\n", inpt1 % inpt2);

	return 0;
}

//20-07-15(수) 끝 2개 품

//20-07-16(목) 시작

#elif 0 // A X B

#include <stdio.h>

int main(void) {
	int inpt1, inpt2;

	scanf("%d %d", &inpt1, &inpt2);
	printf("%d\n", inpt1 * inpt2);

	return 0;
}

#elif 0 // 나머지

#include <stdio.h>

int main(void) {
	int inpt1, inpt2, inpt3;

	scanf("%d %d %d", &inpt1, &inpt2, &inpt3);
	printf("%d\n", (inpt1 + inpt2) % inpt3);
	printf("%d\n", (inpt1 % inpt3 + inpt2 % inpt3) % inpt3);
	printf("%d\n", (inpt1 * inpt2) % inpt3);
	printf("%d\n", ((inpt1 % inpt3) * (inpt2 % inpt3)) % inpt3);

	return 0;
}

#elif 0 //dog

#include <stdio.h>

int main(void) {

	printf("|\\_/|\n");
	printf("|q p|   /}\n");
	printf("( 0 )\"\"\"\\\n");
	printf("|\"^\"`    |\n");
	printf("||_/=\\\\__|\n");

	return 0;
}

#elif 0 // sum

#include <stdio.h>

int main(void) {

	int inpt1, inpt2;

	scanf("%d", &inpt1);
	inpt2 = inpt1 * (inpt1 + 1) / 2;
	printf("%d", inpt2);

	return 0;
}

#elif 0 // sum

#include <stdio.h>

int main(void) {

	int inpt1, inpt2;

	scanf("%d\n%d", &inpt1, &inpt2);

	printf("%d", inpt1 + inpt2);

	return 0;
}


#elif 0 //cat

#include <stdio.h>

int main(void) {

	printf("\\    /\\\n");
	printf(" )  ( \')\n");
	printf("(  /  )\n");
	printf(" \\(__)|\n");

	return 0;
}

#elif 0 // R2

#include <stdio.h>

int main(void) {
	int inpt1, inpt2, inpt3;

	scanf("%d %d", &inpt1, &inpt2);
	inpt3 = inpt2 - inpt1;
	inpt3 = inpt2 + inpt3;
	printf("%d\n", inpt3);

	return 0;
}

#elif 0 // 검증수

#include <stdio.h>

int main(void) {
	int inpt[5];
	int inpt1 = 0;

	scanf("%d %d %d %d %d", &inpt[0], &inpt[1], &inpt[2], &inpt[3], &inpt[4]);

	for (int i = 0; i < 5; ++i) {
		inpt1 += inpt[i] * inpt[i];
	}
	inpt1 = inpt1 % 10;

	printf("%d\n", inpt1);

	return 0;
}

#elif 0 //MS logo

#include <stdio.h>

int main(void) {

	printf("       _.-;;-._\n");
	printf("'-..-'|   ||   |\n");
	printf("'-..-'|_.-;;-._|\n");
	printf("'-..-'|   ||   |\n");
	printf("'-..-'|_.-''-._|\n");

	return 0;
}

#elif 0 // 고려대

#include <stdio.h>

int main(void) {

	printf("고려대학교\n");

	return 0;
}

//20-07-16(목) 끝 10개품

//20-07-17(금) 시작

#elif 0 // 오늘 날짜 

#include <stdio.h>

int main(void) {

	printf("2020-07-17");

	return 0;
}

#elif 0 // 스타후르츠

#include <stdio.h>

int main(void) {

	int day, raise_day, slot, cost, fruit_cnt;

	scanf("%d %d %d %d", &day, &raise_day, &slot, &cost);

	day -= 1;
	fruit_cnt = 0;
	while ((day - raise_day) >= 0) {

		fruit_cnt += slot;

		day = day - raise_day;
	}

	printf("%d", fruit_cnt * cost);

	return 0;
}

#elif 0 // 달달함이 넘쳐흘러 

#include <stdio.h>

int main(void) {

	int a_x, a_y, a_z, b_x, b_y, b_z, c_x, c_y, c_z;

	scanf("%d %d %d\n%d %d %d", &a_x, &a_y, &a_z, &c_x, &c_y, &c_z);

	b_x = c_x - a_z;
	b_y = c_y / a_y;
	b_z = c_z - a_x;

	printf("%d %d %d", b_x, b_y, b_z);

	return 0;
}
// 20-07-17(금) 끝 2시간 c 3개 python 2개 품

// 20-07-18(토) 시작

#elif 0 // 조별과제

#include <stdio.h>

int main(void) {

	int inpt1, t = 0;

	scanf("%d", &inpt1);


	while (inpt1 > 0) {
		t += 1;
		inpt1 -= 5;
	}

	printf("%d", t);

	return 0;
}

#elif 0 // 나는 행복합니다~


#include <stdio.h>

int main(void) {

	int row, col, num, n = 0, m;

	scanf("%d %d %d", &row, &col, &num);

	while (num >= col) {
		n += 1;
		num -= col;
	}
	m = num;
	printf("%d %d", n, m);

	return 0;
}

#elif 0 // 1998년생인 내가 태국에서는 2541년생?!

#include <stdio.h>

int main(void) {

	int bool_gi_year, gap = 543;

	scanf("%d", &bool_gi_year);
	printf("%d", bool_gi_year - gap);

	return 0;
}

// 긴자리 계산 python
// 오늘의 날짜는 python

#elif 0 // X に最も近い値

#include <stdio.h>

int main(void) {
	int x, l, r;

	scanf("%d %d %d", &x, &l, &r);

	if (l <= x && x <= r) {
		printf("%d", x);
	}
	else if (x < l) {
		printf("%d", l);
	}
	else if (x > r) {
		printf("%d", r);
	}


	return 0;
}

#elif 0 // 3 つの整数

#include <stdio.h>

int main(void) {
	int input[3];
	int one_cnt = 0, two_cnt = 0;

	scanf("%d %d %d", &input[0], &input[1], &input[2]);

	for (int i = 0; i < 3; ++i) {
		if (input[i] == 1) {
			one_cnt++;
		}
		else {
			two_cnt++;
		}
	}
	one_cnt > two_cnt ? printf("%d", 1) : printf("%d", 2);

	return 0;
}

#elif 0 // 試験

#include <stdio.h>

int main(void) {
	int input[3];
	int tmp;

	scanf("%d %d %d", &input[0], &input[1], &input[2]);

	for (int i = 0; i < 2; ++i) {
		for (int j = 0; j < 3 - i - 1; ++j) {
			if (input[j] < input[j + 1]) {
				tmp = input[j];
				input[j] = input[j + 1];
				input[j + 1] = tmp;
			}
		}
	}

	printf("%d", input[0] + input[1]);

	return 0;
}

#elif 0 // 鉛筆

#include <stdio.h>

int main(void) {
	int n, a, b, c, d;
	int a_min_i = 0, c_min_i = 0, a_cost = 0, c_cost = 0;

	scanf("%d %d %d %d %d", &n, &a, &b, &c, &d);

	a_min_i = n / a;
	if (n % a > 0) a_min_i++;
	c_min_i = n / c;
	if (n % c > 0) c_min_i++;
	a_cost = a_min_i * b;
	c_cost = c_min_i * d;
	a_cost > c_cost ? printf("%d", c_cost) : printf("%d", a_cost);

	return 0;
}

#elif 0 // ソーシャルゲーム

#include <stdio.h>

int main(void) {
	int a, b, c;
	int day = 0;

	scanf("%d %d %d", &a, &b, &c);

	while (c > 0) {
		day++;
		c -= a;
		if (day % 7 == 0) {
			c -= b;
		}
	}

	printf("%d", day);

	return 0;
}

// A/B 파이썬

// 8진수 2진수 파이썬

#elif 0 // 못품

#include <stdio.h>
#include <math.h>

long long octal_to_binary(int octal)
{
	int decimal = 0, i = 0;
	long long binary = 0;

	while (octal != 0)
	{
		decimal += (octal % 10) * pow(8, i);
		++i;
		octal /= 10;
	}

	i = 1;

	while (decimal != 0)
	{
		binary += (decimal % 2) * i;
		decimal /= 2;
		i *= 10;
	}

	return binary;
}


int main()
{
	int octal;
	scanf("%d", &octal);

	printf("%lld", octal_to_binary(octal));

	return 0;
}

#elif 0 // TV 크기

#include <stdio.h>
#include <math.h>

int main(void) {
	double diag, h_ratio, w_ratio, height, width;


	scanf("%lf %lf %lf", &diag, &h_ratio, &w_ratio);

	width = h_ratio * diag / (sqrt(pow(h_ratio, 2) + pow(w_ratio, 2)));
	height = w_ratio * width / h_ratio;

	printf("%d %d", (int)width, (int)height);


	return 0;
}

#elif 0 // 두 수 비교하기

#include <stdio.h>

int main(void) {
	int a, b;

	scanf("%d %d", &a, &b);

	if (a > b) {
		printf(">");
	}
	else if (a < b) {
		printf("<");
	}
	else {
		printf("==");
	}

	return 0;
}

#elif 0 // 손익분기점

#include <stdio.h>

int main(void) {
	long long a, b, c;
	int cnt;

	scanf("%lld %lld %lld", &a, &b, &c);

	if (b == c || b > c) {
		printf("-1");
		return 0;
	}

	cnt = (int)(a / (c - b));
	cnt++;

	printf("%d", cnt);

	return 0;
}

#elif 0 // 주사위 세개
#include <stdio.h>

int main(void) {
	int a, b, c;
	int prize_money;

	scanf("%d %d %d", &a, &b, &c);

	if (a == b && b == c)	prize_money = 10000 + a * 1000;
	else if (a == b || b == c)	prize_money = 1000 + b * 100;
	else if (a == c)	prize_money = 1000 + a * 100;
	else {
		if (a > b) {
			if (a > c)
				prize_money = a * 100;
			else
				prize_money = c * 100;
		}
		else if (b > c)	prize_money = b * 100;
		else prize_money = c * 100;
	}

	printf("%d", prize_money);

	return 0;
}

#elif 0 // 오븐 시계
#include <stdio.h>

int main(void) {
	int hour, min, gap;
	int hour_cnt, min_cnt;

	scanf("%d %d\n%d", &hour, &min, &gap);

	hour_cnt = gap / 60;
	min_cnt = gap % 60;

	if ((min + min_cnt) > 59) {
		hour_cnt++;
		min = min + min_cnt - 60;
	}
	else min = min + min_cnt;

	if ((hour + hour_cnt) > 23) hour = hour + hour_cnt - 24;
	else hour = hour + hour_cnt;

	printf("%d %d", hour, min);

	return 0;
}

// 20-07-18 끝 c 13 python 4 = 17 품 브론즈3 승급 약8시간

//20-07-18 2차시작 21:30

#elif 0 //인공지능 시계

#include <stdio.h>

int main(void) {
	int hour, min, sec, gap;
	int hour_cnt, min_cnt, sec_cnt;

	scanf("%d %d %d\n%d", &hour, &min, &sec, &gap);

	hour_cnt = gap / 3600;
	hour_cnt = hour_cnt % 24;
	gap = gap % 3600;
	min_cnt = gap / 60;
	sec_cnt = gap % 60;

	if ((sec + sec_cnt) > 59) {
		min_cnt++;
		if (min_cnt > 59) {
			hour_cnt++;
			if (hour_cnt > 23) hour_cnt = hour_cnt - 24;

			min_cnt = min_cnt - 60;
		}
		sec = sec + sec_cnt - 60;
	}
	else sec = sec + sec_cnt;

	if ((min + min_cnt) > 59) {
		hour_cnt++;
		if (hour_cnt > 23) hour_cnt = hour_cnt - 24;

		min = min + min_cnt - 60;
	}
	else min = min + min_cnt;

	if ((hour + hour_cnt) > 23) hour = hour + hour_cnt - 24;
	else hour = hour + hour_cnt;

	printf("%d %d %d", hour, min, sec);


	return 0;
}

#elif 0 //곱셈

#include <stdio.h>

int main(void) {
	int a, b;
	int total, one, ten, hnd;

	scanf("%d\n%d", &a, &b);

	total = a * b;
	hnd = a * (b / 100);
	ten = a * ((b / 10) % 10);
	one = a * (b % 10);

	printf("%d\n%d\n%d\n%d", one, ten, hnd, total);

	return 0;
}

#elif 0 //윤년

#include <stdio.h>

int main(void) {
	int year;

	scanf("%d", &year);

	if (!(year % 4) && (year % 100) || !(year % 400))
		printf("1");
	else printf("0");

	return 0;
}

#elif 0 // 平均点

#include <stdio.h>

int main(void) {
	int student_seiseki[5];
	int total = 0;

	scanf("%d\n%d\n%d\n%d\n%d",
		&student_seiseki[0], &student_seiseki[1],
		&student_seiseki[2], &student_seiseki[3], &student_seiseki[4]);

	for (int i = 0; i < 5; ++i) {
		if (student_seiseki[i] < 40) student_seiseki[i] = 40;
		total += student_seiseki[i];
	}

	printf("%d", total / 5);

	return 0;
}

// 20-07-18 23:00 끝 c 4개 품  23:00~24:00 한숨잠

// 20-07-19 03:30 1차 시작

#elif 0 // 宿題 (Homework)

#include <stdio.h>

int main(void) {
	int l, g_d, s_d, g_d_per_day, s_d_per_day;

	scanf("%d\n%d\n%d\n%d\n%d", &l, &g_d, &s_d, &g_d_per_day, &s_d_per_day);

	while (g_d > 0 || s_d > 0) {
		l--;
		g_d -= g_d_per_day;
		s_d -= s_d_per_day;
	}

	printf("%d", l);

	return 0;
}

#elif 0 // 宿題 (Homework) 다른방식으로 풀기

#include <stdio.h>

int main(void) {
	int l, g_d, s_d, g_d_per_day, s_d_per_day;
	int g_day = 0, s_day = 0;

	scanf("%d\n%d\n%d\n%d\n%d", &l, &g_d, &s_d, &g_d_per_day, &s_d_per_day);


	g_day = g_d / g_d_per_day;
	if (g_d % g_d_per_day != 0) g_day += 1;
	s_day = s_d / s_d_per_day;
	if (s_d % s_d_per_day != 0) s_day += 1;

	l -= g_day >= s_day ? g_day : s_day;


	printf("%d", l);

	return 0;
}

#elif 0 // 상근날드

#include <stdio.h>

int main(void) {
	int burger[3], drink[2];
	int rst_burger, rst_drink, rst_total;

	scanf("%d\n%d\n%d\n%d\n%d", &burger[0], &burger[1], &burger[2], &drink[0], &drink[1]);

	if (burger[0] < burger[1]) {
		if (burger[0] < burger[2]) rst_burger = burger[0];
		else rst_burger = burger[2];
	}
	else if (burger[1] < burger[2]) rst_burger = burger[1];
	else rst_burger = burger[2];

	if (drink[0] >= drink[1]) rst_drink = drink[1];
	else rst_drink = drink[0];

	rst_total = rst_burger + rst_drink - 50;

	printf("%d", rst_total);


	return 0;
}

//python 사파리월드

#elif 0 // 시험 점수

#include <stdio.h>

int main(void) {
	int mk[4], ms[4];
	int mk_total = 0, ms_total = 0;

	scanf("%d %d %d %d\n%d %d %d %d",
		&mk[0], &mk[1], &mk[2], &mk[3],
		&ms[0], &ms[1], &ms[2], &ms[3]);

	for (int i = 0; i < 4; ++i) {
		mk_total += mk[i];
		ms_total += ms[i];
	}

	if (mk_total >= ms_total) printf("%d", mk_total);
	else printf("%d", ms_total);

	return 0;
}

#elif 0 // 수학은 체육과목 입니다 2

#include <stdio.h>

int main(void) {
	int n;
	int rst = 0;

	scanf("%d", &n);

	if (n < 6) printf("%d", n);
	else {
		switch ((n - 6) % 8)
		{
		case 3:
			rst = 1;
			break;
		case 2:
		case 4:
			rst = 2;
			break;
		case 1:
		case 5:
			rst = 3;
			break;
		case 0:
		case 6:
			rst = 4;
			break;
		case 7:
			rst = 5;
			break;
		default:
			break;
		}

		printf("%d", rst);
	}

	return 0;
}

// A/B - 3 python

#elif 0 // 연세대학교

#include <stdio.h>

int main(void) {
	int n;
	scanf("%d", &n);
	if (n == 0) printf("YONSEI");
	else printf("Leading the Way to the Future");

	return 0;
}

#elif 0 // 수찬은 마린보이야!!

#include <stdio.h>

int main(void) {
	int n;
	int record[100];
	int total = 0;
	double avg, ex_val = 0;

	for (int i = 0; i < 100; ++i) {
		record[i] = -1;
	}

	scanf("%d", &n);

	if (n == 0) {
		printf("divide by zero");
		return 0;
	}

	for (int i = 0; i < n; ++i) {
		scanf("%d", &record[i]);
		total += record[i];
		ex_val += (double)record[i] / (double)n;
	}

	avg = (double)total / (double)n;

	printf("%.2lf", avg / ex_val);


	return 0;
}

// 20-07-19 07:00 1차 끝 c 6 python 2 3시간 30분 8개

// 20-07-19 07:50 2차 시작 (밥 먹고 왔음)

#elif 0 // 전자레인지

#include <stdio.h>

int main(void) {
	int init, goal, frozen_heat_t, melt_t, heat_t;
	int loading_t = 0;

	scanf("%d\n%d\n%d\n%d\n%d", &init, &goal, &frozen_heat_t, &melt_t, &heat_t);

	while (init < 0) {
		loading_t += frozen_heat_t;
		init++;
	}

	if (init == 0) loading_t += melt_t;

	while (init < goal) {
		loading_t += heat_t;
		init++;
	}

	printf("%d", loading_t);


	return 0;
}

// 20-07-19 08:00 2차 끝 c 1문제 (그 후 잠)

// 20-07-19 13:20 3차 시작 차 안에서

#elif 0 // Coupons

#include <stdio.h>

int main(void) {
	int n;
	double inpt_price;

	scanf("%d", &n);

	if (n == 0) {
		return 0;
	}

	for (int i = 0; i < n; ++i) {
		scanf("%lf", &inpt_price);
		printf("$%.2lf", inpt_price * 0.8);
		if (i < n - 1) printf("\n");
	}

	return 0;
}

#elif 0 // 폰 노이만과 파리

#include <stdio.h>

int main(void) {
	int s, t, d;

	scanf("%d %d %d", &s, &t, &d);

	printf("%d", d / (2 * s) * t);

	return 0;
}

// 공백 없는 A+B python

// 20-07-19 14:00 3차 끝 C 2 python 2 40분 총 3문제  3699위

// 20-07-19 14:13 4차 시작 3701위 브론즈 3문제 시작

#elif 0 // 별 찍기 - 1

#include <stdio.h>

int main(void) {
	int n;

	scanf("%d", &n);

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j <= i; ++j) {
			printf("*");
		}
		printf("\n");
	}

	return 0;
}

#elif 0 // N 찍기

#include <stdio.h>

int main(void) {
	int n;

	scanf("%d", &n);

	for (int i = 0; i < n; ++i) {
		printf("%d", i + 1);
		printf("\n");
	}

	return 0;
}

#elif 0 // 구구단

#include <stdio.h>

int main(void) {
	int n;

	scanf("%d", &n);

	for (int i = 1; i <= 9; ++i) {
		printf("%d * %d = %d\n", n, i, n * i);
	}

	return 0;
}

#elif 0 // 기찍 N

#include <stdio.h>

int main(void) {
	int n;

	scanf("%d", &n);

	for (int i = n; i > 0; --i) {
		printf("%d", i);
		printf("\n");
	}

	return 0;
}

#elif 0 // 별찍기 -2

#include <stdio.h>

int main(void) {
	int n;

	scanf("%d", &n);

	for (int i = 0; i < n; ++i) {
		for (int j = 1; j <= n; ++j) {
			if (j < n - i) printf(" ");
			else printf("*");
		}
		printf("\n");
	}

	return 0;
}

// 20-07-19 14:13 - 14:33 4차 끝 c 5문제 20분

// 20-07-19 21:44 5차 시작 단머 스터디 후 휴식 후 시작

#elif 0 // 세 수

#include <stdio.h>

int main(void) {
	int input[3];
	int tmp;

	scanf("%d %d %d", &input[0], &input[1], &input[2]);

	for (int i = 0; i < 2; ++i) {
		for (int j = 0; j < 3 - i - 1; ++j) {
			if (input[j] < input[j + 1]) {
				tmp = input[j];
				input[j] = input[j + 1];
				input[j + 1] = tmp;
			}
		}
	}

	printf("%d", input[1]);

	return 0;
}

// 20-07-19 21:50 5차 끝 한 문제만 품

// 20-07-20 04:20 1차 시작

#elif 0 // X보다 작은 수

#include <stdio.h>

int main(void) {
	int n, x;
	int n_arr[10000], smaller_than_x_arr[10000];
	int j = 0;

	for (int i = 0; i < 10000; ++i) {
		n_arr[i] = -1;
		smaller_than_x_arr[i] = -1;
	}

	scanf("%d %d", &n, &x);

	for (int i = 0; i < n; ++i) {
		scanf("%d", &n_arr[i]);
		if (n_arr[i] < x) {
			smaller_than_x_arr[j] = n_arr[i];
			j++;
		}
	}

	for (int i = 0; i < j; ++i) {
		printf("%d ", smaller_than_x_arr[i]);
	}


	return 0;
}

#elif 0 // 별 찍기 - 3

#include <stdio.h>

int main(void) {
	int n;

	scanf("%d", &n);

	for (int i = n; i > 0; --i) {
		for (int j = 0; j < i; ++j) {
			printf("*");
		}
		printf("\n");
	}

	return 0;
}

#elif 0 // A+B - 3

#include <stdio.h>

int main(void) {
	int n, a, b;

	scanf("%d", &n);

	if (n == 0) {
		return 0;
	}

	for (int i = 0; i < n; ++i) {
		scanf("%d %d", &a, &b);
		printf("%d\n", a + b);
	}

	return 0;
}

#elif 0 // 별 찍기 - 4

#include <stdio.h>

int main(void) {
	int n;

	scanf("%d", &n);

	for (int i = n; i > 0; --i) {
		for (int j = 0; j < n; ++j) {
			if (j < n - i) printf(" ");
			else printf("*");
		}
		printf("\n");
	}

	return 0;
}

#elif 0 // A+B - 5

#include <stdio.h>

int main(void) {
	int a, b;

	while (scanf("%d %d", &a, &b)) {
		if (a == 0 && b == 0) return 0;
		printf("%d\n", a + b);
	}

	return 0;
}

#elif 0 // A+B - 7

#include <stdio.h>

int main(void) {
	int n, a, b;

	scanf("%d", &n);

	if (n == 0) {
		return 0;
	}

	for (int i = 0; i < n; ++i) {
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d\n", i + 1, a + b);
	}

	return 0;
}

// 20-07-20 04:20 - 04: 50 1차 끝 c 6문제 소요시간: 30분

// 20-07-20 05:52 2차 시작 별찍기 마스터 할 예정

#elif 0 // 별 찍기 - 5

#include <stdio.h>

int main(void) {
	int n;

	scanf("%d", &n);

	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= 2 * n; ++j) {
			if (n - i < j && j < n + i)	printf("*");
			else if (n - i >= j) printf(" ");
			else printf("");
		}
		if (i != n)	printf("\n");
	}

	return 0;
}

#elif 0 // 별 찍기 - 6

#include <stdio.h>

int main(void) {
	int n;

	scanf("%d", &n);

	for (int i = n; i >= 1; --i) {
		for (int j = 1; j <= 2 * n; ++j) {
			if (n - i < j && j < n + i)	printf("*");
			else if (n - i >= j) printf(" ");
			else printf("");
		}
		if (i != 1)	printf("\n");
	}

	return 0;
}

#elif 0 // 별 찍기 - 7

#include <stdio.h>

int main(void) {
	int n;

	scanf("%d", &n);

	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= 2 * n; ++j) {
			if (n - i < j && j < n + i)	printf("*");
			else if (n - i >= j) printf(" ");
			else printf("");
		}
		printf("\n");
	}

	for (int i = n - 1; i >= 1; --i) {
		for (int j = 1; j <= 2 * n; ++j) {
			if (n - i < j && j < n + i)	printf("*");
			else if (n - i >= j) printf(" ");
			else printf("");
		}
		if (i != 1)	printf("\n");
	}

	return 0;
}

#elif 0 // 별 찍기 - 8

#include <stdio.h>

int main(void) {
	int n;

	scanf("%d", &n);

	for (int i = n; i >= 1; --i) {
		for (int j = 1; j <= 2 * n; ++j) {
			if (i == 1 && j != 2 * n) printf("*");
			else if (n - i + 1 < j && j < n + i)	printf(" ");
			else printf("*");
		}
		printf("\n");
	}

	for (int i = 2; i <= n; ++i) {
		for (int j = 1; j <= 2 * n; ++j) {
			if (n - i + 1 < j && j < n + i)	printf(" ");
			else printf("*");
		}
		if (i != n)	printf("\n");
	}

	return 0;
}

#elif 0 // 별 찍기 - 9

#include <stdio.h>

int main(void) {
	int n;

	scanf("%d", &n);

	for (int i = n; i >= 1; --i) {
		for (int j = 1; j <= 2 * n; ++j) {
			if (n - i < j && j < n + i)	printf("*");
			else if (n - i >= j) printf(" ");
			else printf("");
		}
		printf("\n");
	}

	for (int i = 2; i <= n; ++i) {
		for (int j = 1; j <= 2 * n; ++j) {
			if (n - i < j && j < n + i)	printf("*");
			else if (n - i >= j) printf(" ");
			else printf("");
		}
		if (i != n)	printf("\n");
	}

	return 0;
}

#elif 0 // 별 찍기 - 12

#include <stdio.h>

int main(void) {
	int n;

	scanf("%d", &n);

	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= 2 * n; ++j) {
			if (j > n) printf("");
			else if (n - i < j && j < n + i) printf("*");
			else if (n - i >= j) printf(" ");
			else printf("");
		}
		printf("\n");
	}

	for (int i = n - 1; i >= 1; --i) {
		for (int j = 1; j <= 2 * n; ++j) {
			if (j > n) printf("");
			else if (n - i < j && j < n + i) printf("*");
			else if (n - i >= j) printf(" ");
			else printf("");
		}
		if (i != 1)	printf("\n");
	}

	return 0;
}

#elif 0 // 별 찍기 - 13

#include <stdio.h>

int main(void) {
	int n;

	scanf("%d", &n);

	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= 2 * n; ++j) {
			if (j < n) printf("");
			else if (n - i < j && j < n + i) printf("*");
			else if (n - i >= j) printf(" ");
			else printf("");
		}
		printf("\n");
	}

	for (int i = n - 1; i >= 1; --i) {
		for (int j = 1; j <= 2 * n; ++j) {
			if (j < n) printf("");
			else if (n - i < j && j < n + i) printf("*");
			else if (n - i >= j) printf(" ");
			else printf("");
		}
		if (i != 1)	printf("\n");
	}

	return 0;
}

// 20-07-20 05:52 - 07:25 2차 끝 1+ 인 사람이 푼 별찍기 다 품 c 7문제 1시간 33분 약 90분

// 20-07-20 11:47 3차 시작 나보다 밑이고 1++인 사람 문제 다 풀기 시작

#elif 0 // 홍익대학교

#include <stdio.h>

int main(void) {
	int year;
	scanf("%d", &year);
	printf("%d", year - 1946);

	return 0;
}

// 단어의 개수 python

// 20-07-20 11:47 - 12:35 3차 끝 c 1문제 python 1문제 총 2문제 약 50분

// 20-07-21 04:29 1차 시작 나보다 밑이고 1++인 사람 문제 다 풀기 시작

// 더하기 사이클 python 

// 20-07-21 07:00 거의 2시간 쏟았는데 못품 ㅆㅃ

// 20-07-21 09:36 더하기 사이클 python 다시 풀기 시작

// 20-07-21 20:12 더하기 사이클 python으로 품 20:39

// 21:05 단어공부 python 22:51 인공지능방 사람들 도움으로 해결함 ;ㅅ;

// 20-07-22 00:24 1차 시작

#elif 0 // Welcome

#include <stdio.h>

int main(void) {

	printf(".  .   .\n");
	printf("|  | _ | _. _ ._ _  _\n");
	printf("|/\\|(/.|(_.(_)[ | )(/.\n");

	return 0;
}

// python ??!

// python 시험 성적

// 20-07-22 00:24 - 00:54 1차 끝 30분 3문제

// 20-07-22 08:39 2차 시작

#elif 0 // 알람 시계

#include <stdio.h>

int main(void) {
	int h, m;
	int gap = 45;

	scanf("%d %d", &h, &m);
	m -= gap;
	if (m < 0) {
		h -= 1;
		if (h < 0) h += 24;
		m += 60;
	}

	printf("%d %d", h, m);

	return 0;
}

#elif 0 // 최소, 최대

#include <stdio.h>

int input[1000000];

int main(void) {
	int n;
	int max = 0, min = 0;

	scanf("%d\n", &n);

	for (int i = 0; i < n; ++i) {
		scanf("%d", &input[i]);
		if (i == 0) {
			max = input[0];
			min = input[0];
		}
		else {
			if (input[i] > max) max = input[i];
			else if (input[i] < min) min = input[i];
		}
	}

	printf("%d %d", min, max);

	return 0;
}


#elif 0 // A+B - 4

#include <stdio.h>

int main(void) {
	int a, b;

	while (scanf("%d %d", &a, &b) != EOF) {
		if (a < 1 || b < 1 || 9 < a || 9 < b) return 0;
		printf("%d\n", a + b);
	}

	return 0;
}

#elif 0 // A+B - 8

#include <stdio.h>

int main(void) {
	int n, a, b;

	scanf("%d", &n);

	if (n == 0) {
		return 0;
	}

	for (int i = 0; i < n; ++i) {
		scanf("%d %d", &a, &b);
		if (a < 1 || b < 1 || 9 < a || 9 < b) return 0;
		printf("Case #%d: %d + %d = %d\n", i + 1, a, b, a + b);
	}

	return 0;
}

// 30분 식사

#elif 0 // 그대로 출력하기

#include <stdio.h>

int main(void) {
	char c;

	while ((c = getchar()) != EOF) {
		putchar(c);
	}

	return 0;
}

#elif 0 // 최댓값

#include <stdio.h>

int main(void) {
	int n = 9;
	int input[9];
	int max, max_idx;

	for (int i = 0; i < 9; ++i) {
		scanf("%d", &input[i]);
		if (i == 0) {
			max = input[0];
			max_idx = 0;
		}
		else if (input[i] > max) {
			max = input[i];
			max_idx = i;
		}
	}

	printf("%d\n%d", max, max_idx + 1);

	return 0;
}

// 20-07-22 08:39 - 10:14 2차 끝 , 중간에 식사시간 30분 6문제 1시간 걸림

// 20-07-22 10:14 3차 시작 중간에 휴식 + 식사 약 2시간

#elif 0 // 문자열 반복

#include <stdio.h>

int main(void) {
	int n, iter;
	char str[25];
	int j = 0;

	scanf("%d", &n);

	for (int i = 0; i < n; ++i) {
		scanf("%d %s", &iter, str);
		while (str[j] != '\0') {
			for (int k = 0; k < iter; ++k) {
				printf("%c", str[j]);
			}
			j++;
		}
		printf("\n");
		j = 0;
	}

	return 0;
}
#elif 0 // 음계

#include <stdio.h>

int main(void) {
	int input[8];
	int input_as[8];
	int input_de[8];
	int tmp;
	int flag = 0;

	for (int i = 0; i < 8; ++i) {
		scanf("%d", &input[i]);
		input_as[i] = input[i];
		input_de[i] = input[i];
	}


	for (int i = 0; i < 7; ++i) {
		for (int j = 0; j < 8 - i - 1; ++j) {
			if (input_as[j] > input_as[j + 1]) {
				tmp = input_as[j];
				input_as[j] = input_as[j + 1];
				input_as[j + 1] = tmp;
			}
		}
	}

	for (int i = 0; i < 7; ++i) {
		for (int j = 0; j < 8 - i - 1; ++j) {
			if (input_de[j] < input_de[j + 1]) {
				tmp = input_de[j];
				input_de[j] = input_de[j + 1];
				input_de[j + 1] = tmp;
			}
		}
	}

	for (int i = 0; i < 8; ++i) {
		flag = 1;
		if (input_as[i] != input[i]) {
			flag = 2;
			break;
		}
	}

	if (flag == 1) {
		printf("ascending\n");
		return 0;
	}

	for (int i = 0; i < 8; ++i) {
		if (input_de[i] != input[i]) {
			flag = 1;
			break;
		}
	}

	if (flag == 2) {
		printf("descending\n");
	}
	else {
		printf("mixed\n");
	}

	return 0;
}

// 숫자의 개수

// OX퀴즈 python

// 20-07-22 10:14 - 14:14 3차 시작 , 중간에 휴식 + 식사 약 2시간 c 2 python 2 총 4개 은장 획득 브론즈1 승급

// 20-07-22 18:20 4차 시작 금장 따고 저녁 먹는다

// 상수 python

// 나머지 python

// 알파벳 찾기 python

// 평균 python

// 20-07-22 18:20 - 19:51 4차 끝 금장 땄다. 약 1시간 30분 걸림 밥 먹으러 감

// 100개 풀기 완료

// 20-07-24 21:20 피보나치 함수

#elif 0 
#include <stdio.h>

int zero_cnt = 0;
int one_cnt = 0;

int fibonacci(int n) {
	if (n == 0) {
		zero_cnt++;
		return 0;
	}
	else if (n == 1) {
		one_cnt++;
		return 1;
	}
	else {
		return fibonacci(n - 1) + fibonacci(n - 2);
	}
}

int main(void) {
	int n, fibo_inpt;

	scanf("%d\n", &n);

	for (int i = 0; i < n; ++i) {
		scanf("%d", &fibo_inpt);
		fibonacci(fibo_inpt);
		printf("%d %d\n", zero_cnt, one_cnt);
		zero_cnt = 0;
		one_cnt = 0;
	}

	return 0;
}

// 20-08-21(금) 02:36 시작

// python 팩토리얼, 

#elif 0 // 피보나치 수

#include<stdio.h> 

int fib(int n)
{

	int f[45];
	int i;

	f[0] = 0;
	f[1] = 1;

	for (i = 2; i <= n; i++)
		f[i] = f[i - 1] + f[i - 2];

	return f[n];
}

int main(void)
{
	int n;
	scanf("%d", &n);
	printf("%d", fib(n));
	return 0;
}

#elif 0 // 초콜릿 자르기

#include <stdio.h>

int main(void) {
	int n, m;

	scanf("%d %d", &n, &m);

	printf("%d", n * m - 1);

	return 0;
}

#elif 0 // 윷놀이

#include <stdio.h>

int main(void) {
	int arr[3][4];
	int one_cnt[3], rst_flag = -1;

	for (int i = 0; i < 3; ++i) {
		scanf("%d %d %d %d", &arr[i][0], &arr[i][1], &arr[i][2], &arr[i][3]);

		one_cnt[i] = 0;
		for (int j = 0; j < 4; ++j) {
			if (arr[i][j] == 1)
				one_cnt[i]++;
		}

	}

	for (int i = 0; i < 3; ++i) {

		if (one_cnt[i] == 4) {
			printf("E\n");
		}
		else if (one_cnt[i] == 3) {
			printf("A\n");
		}
		else if (one_cnt[i] == 2) {
			printf("B\n");
		}
		else if (one_cnt[i] == 1) {
			printf("C\n");
		}
		else {
			printf("D\n");
		}

	}

	return 0;
}

#elif 0 // 지능형 기차

#include <stdio.h>

int main(void) {
	int i, max;
	int gOff[4] = { 0, };
	int gInn[4] = { 0, };
	int total = 0;
	int maxCmp[4] = { 0, };

	for (i = 0; i < 4; i++) {
		scanf("%d %d", &gOff[i], &gInn[i]);
	}

	for (i = 0; i < 4; i++) {
		total += gInn[i] - gOff[i];
		maxCmp[i] = total;
		if (i == 0) {
			max = maxCmp[i];
		}
		else {
			max = maxCmp[i] > max ? maxCmp[i] : max;
		}
	}
	printf("%d\n", max);

	return 0;
}

#elif 0 //오르막길 (USPON)

#include <stdio.h>

int main(void) {
	int value_n = 0;
	int arr[1000] = { 0 };
	int j, k;
	int start = 0, end = 0;
	int sharpest = 0, tmp_sharpest = 0;

	scanf("%d\n", &value_n);

	for (j = 0; j < value_n; ++j) {
		scanf("%d", &arr[j]);
	}

	for (k = start; k < value_n - 1; ++k) {

		if (arr[k] < arr[k + 1]) {
			end++;
		}
		else {
			if (start == end) {
				start++; end++;
			}
			else {
				if (sharpest == 0) {
					sharpest = arr[end] - arr[start];
				}
				else {
					tmp_sharpest = arr[end] - arr[start];
					sharpest = tmp_sharpest > sharpest ? tmp_sharpest : sharpest;
				}
				start = end + 1;
				end = start;
			}

		}
		tmp_sharpest = arr[end] - arr[start];
		sharpest = tmp_sharpest > sharpest ? tmp_sharpest : sharpest;
	}

	printf("%d\n", sharpest);

	return 0;

}

// 20-08-21(금) 08:36 끝  6시간 6문제

// 20-08-22(토) 15:57 시작

#elif 1 // 별찍기 - 16

#include <stdio.h>

int main(void) {
	int n;

	scanf("%d", &n);

	for (int i = 0; i < n; ++i) {
		for (int j = 1; j <= n+i; ++j) {
			printf("*");	
		}
		printf("\n");
	}
	

	return 0;
}



#endif