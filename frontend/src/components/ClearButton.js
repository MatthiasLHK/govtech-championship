import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';

function ClearButton() {

    const clearData = () => {
        axios.get("/clearData").then(console.log("Cleared all data!"));
        setTimeout(() => {  window.location.reload(false); }, 3000);
    }

    return (
        <Button type="button" class="btn btn-warning" onClick={()=>clearData()}>Clear all data!</Button>
    )
}

export default ClearButton;