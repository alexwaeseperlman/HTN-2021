import logo from './logo.svg';
import './App.css';
import Input from "./components/Input"
import image from "./assets/image.png"

function App() {
  return (
    <div className="App">
      <hl className="title">ARCrouter</hl>
      <div>
        <Input />
        <img className="image" src={image} width="30%" height="30%" />
      </div>
    </div>
  );
}

export default App;
