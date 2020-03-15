var sum=0,n,x=[],y=[];
n=prompt('Количемтво n: ');
function ploshad()
{
  for (var i=0; i<n;i++)
  {
   sum=sum+(x[i]*y[i+1]-y[i]*x[i+1]);
  }
}
for (var i=0; i<n;i++)
{
  x[i]=Math.floor(Math.random()*100-50);
  y[i]=Math.floor(Math.random()*100-50);
}
alert(x);
alert(y);
x[n]=x[0];
y[n]=y[0];

ploshad();
alert('Площадь многоуголника: '+sum);