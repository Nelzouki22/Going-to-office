# Going to office
Problem
Alice has the following two types of taxis:

Online taxi: It can be booked by using an online application from phones 
Classic taxi: It can be booked anywhere on the road
The online taxis cost Oc
 for the first Of
 km and Od
 for every km afterward. The classic taxis travel at a speed of Cs
 km per minute. The cost of classic taxis are Cb
, Cm
, and Cd
 that represents the base fare, cost for every minute that is spent in the taxi, and cost for each kilometer that you ride.

You are going to the office from your home. Your task is to minimize the cost that you are required to pay. The distance from your home to the office is D. You are required to select whether you want to use online or classic taxis to go to your office. If both the taxis cost the same, then you must use an online taxi.

Input format

First line: Single integer D
 that denotes the distance from your house to the office
Next line: Three integers Oc
 , Of
 , and Od
  
Next line: Four integers Cs
 , Cb
 , Cm
 , and Cd
Output format

If you select an online taxi to travel, then print a string 'Online Taxi'. Otherwise, select 'Classic Taxi'. You can print this string in a new, single line.

Constraints

1 ≤
 D, Oc, Of, Od, Cs, Cb, Cm, Cd
 ≤
 109

Sample Input
13
6 7 4
4 2 1 2
Sample Output
Online Taxi
Time Limit: 1
Memory Limit: 64
Source Limit:
Explanation
If Felix choose to use Online Taxi, it will cost Felix a total of 6+(13−7)×4=30

While the classic taxi will cost Felix a total of 2+⌊134⌋×1+13×2=31

Therefore Felix will choose Online Taxi over Classic Taxi

الذهاب إلى المكتب تملك أليس نوعين من سيارات الأجرة:

التاكسي عبر الإنترنت: يمكن حجزه باستخدام تطبيق عبر الهواتف.
التاكسي الكلاسيكي: يمكن حجزه في أي مكان على الطريق.
تكلفة التاكسي عبر الإنترنت هي Oc لأول Of كيلومتر، و Od لكل كيلومتر إضافي. أما التاكسي الكلاسيكي فيسير بسرعة Cs كيلومتر في الدقيقة. وتكاليف التاكسي الكلاسيكي هي Cb (تكلفة ثابتة)، Cm (تكلفة لكل دقيقة في التاكسي)، و Cd (تكلفة لكل كيلومتر تقطعه).

مهمتك هي تقليل التكلفة التي ستدفعها للذهاب من منزلك إلى المكتب. المسافة من منزلك إلى المكتب هي D. يجب عليك تحديد ما إذا كنت ستستخدم التاكسي عبر الإنترنت أو التاكسي الكلاسيكي. إذا كانت التكلفة متساوية، فيجب عليك استخدام التاكسي عبر الإنترنت.

المدخلات:
السطر الأول: عدد صحيح D يمثل المسافة من منزلك إلى المكتب.
السطر الثاني: ثلاثة أرقام صحيحة Oc، Of، Od (معلومات التاكسي عبر الإنترنت).
السطر الثالث: أربعة أرقام صحيحة Cs، Cb، Cm، Cd (معلومات التاكسي الكلاسيكي).
المخرجات:
إذا اخترت التاكسي عبر الإنترنت، اطبع "Online Taxi"، وإذا اخترت التاكسي الكلاسيكي، اطبع "Classic Taxi".
القيود:
1 ≤ D, Oc, Of, Od, Cs, Cb, Cm, Cd ≤ 10^9

المدخلات التجريبية:
Copy code
13
6 7 4
4 2 1 2
المخرجات التجريبية:
Copy code
Online Taxi
