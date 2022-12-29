import React, {useState, useEffect} from "react";
import axios, { all } from "axios";

const ApiUrl = 'http://127.0.0.1:8000/api/items/'


export default props => {

    const [items, setItems] = useState(null)

    const ItemsApi = () => {
        axios.get(ApiUrl)
        .then(response => {
            const allItems = response.data
            setItems(allItems)
        })
        .catch(error => console.error(error))
    }
    
    useEffect(ItemsApi)

    return(
        <div className="content">
            item
        </div>
    )
}
