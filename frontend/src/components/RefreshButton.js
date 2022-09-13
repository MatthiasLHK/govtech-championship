import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css';

function RefreshButton() {

    function refreshPage() {
        window.location.reload(false)
    }

    return (
        <Button onClick={refreshPage}>Refresh Data!</Button>
    )
}

export default RefreshButton;