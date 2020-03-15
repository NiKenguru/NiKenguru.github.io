var n,m,k=0;
n=prompt('Введите количество столбцов: ');
m=prompt('Введите количество строк: ');
function Matrix(n,m){
 
  var f= [];
for (var i=0;i<n;i++)
{ f[i]= [];
  for (var j=0;j<m;j++)
  {
    f[i][j]=Math.random()*100-50;
  }
}
 return f;
}

function Proverka(arr)
{
for (var i=0;i<n;i++)
{  
  for (var j=0;j<m;j++)
  {
    if (Math.abs(arr[i][j])>k)
    {
      k=Math.abs(arr[i][j]);
    }
  }
}
} 
var arr=Matrix(n,m);
 alert('Матрица');
alert(arr);
Proverka(arr);
alert('Наибольшее число: '+k);
alert('Матрица');
  for (var i = 0; i < n; i++)
     { 
       for (var j = 0; j <m; j++) {arr[i][j] = arr[i][j]/k;}
     }
alert(arr);


  