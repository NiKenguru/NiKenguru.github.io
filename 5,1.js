var f=[],n;
n=prompt('Введите количество n: ');
for (var i=1;i<=n;i++)
{ f[i]=0;
  for (var j=1;j<=i+1;j++)
  {
    f[i]=f[i]+1/(i*i+j);
  }
  alert('f'+i+': ',f[i]);
}