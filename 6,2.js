function getRandomInt(max) {
return Math.floor(Math.random() * Math.floor(max));
}
var arr=[],n,sum=0;
n=prompt('введите число n: ');
for(i=0;i<=n;i++)
{
arr[i]=getRandomInt(100);
}
alert (arr);
for (var i=1;i<=n;i++)
{
sum=sum+(Math.pow((Math.sqrt(Math.abs(arr[i]))-arr[i]),2));
}