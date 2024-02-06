import styles from './App.module.css';


const age = 15;
if (age>=18){
  console.log("Over age");
}
else{
  console.log("Under age");
}

function App() {
  const age = 15;
  if (age>=18){
    return <h1>Over age</h1>
  }else{
  return (
    <div className={styles.App}>
      UNDER AGE!
    </div>
  );
  }
}



// const Job = (props) => {
//   return (
//    <div>
//     <h1>{props.salary}</h1>
//     <h1>{props.position}</h1>
//     <h1>{props.company}</h1>
    
//    </div>
//   );
// };

export default App;
