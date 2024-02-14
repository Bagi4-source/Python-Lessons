import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';
import {NextUIProvider} from "@nextui-org/react";

const root = ReactDOM.createRoot(
    document.getElementById('root') as HTMLElement
);
root.render(
    <React.StrictMode>
        <NextUIProvider>
            <App/>
        </NextUIProvider>
    </React.StrictMode>
);
