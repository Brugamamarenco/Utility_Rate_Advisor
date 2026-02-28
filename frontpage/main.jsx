export function display(){
    <div> 

    </div>
}

export function actionLog(){
    <div> 
    </div>
}

//used for creating the item
export function action(item){
    return (
    <div> 
        <h1> {item.product} </h1>
        <h3> ${item.cost} </h3>
    </div>
    )
}

//function to render 
const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
<action product="pug" cost="500" />
);



