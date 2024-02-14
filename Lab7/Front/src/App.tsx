import {createBrowserRouter, RouterProvider} from "react-router-dom";
import {NextUIProvider} from "@nextui-org/react";
import {Main} from "./pages";

const router = createBrowserRouter([
    {
        path: "/",
        element: <Main/>
    }
]);


function App() {
    return <NextUIProvider>
        <div className={"container mx-auto my-6"}>
            <RouterProvider router={router}/>
        </div>
    </NextUIProvider>
}

export default App;
