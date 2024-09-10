import math

# إدخال البيانات
D = int(input())
Oc, Of, Od = map(int, input().split())
Cs, Cb, Cm, Cd = map(int, input().split())

# حساب تكلفة التاكسي عبر الإنترنت
online_cost = Oc
if D > Of:
    online_cost += (D - Of) * Od

# حساب تكلفة التاكسي الكلاسيكي
classic_minutes = math.ceil(D / Cs)
classic_cost = Cb + classic_minutes * Cm + D * Cd

# تحديد الأرخص
if online_cost <= classic_cost:
    print("Online Taxi")
else:
    print("Classic Taxi")

