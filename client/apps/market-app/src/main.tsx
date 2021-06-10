import { StrictMode } from 'react';
import * as ReactDOM from 'react-dom';

import { BrowserRouter } from 'react-router-dom';

import {
  SIGNIN_USER_KEY,
  getSignInUserDetails,
} from '@client/market-app/sign-in';

import App from './app/app';
import { configureStore } from '@reduxjs/toolkit';

const store = configureStore({
  reducer: {
    [SIGNIN_USER_KEY]: getSignInUserDetails,
  },
});

ReactDOM.render(
  <StrictMode>
    <BrowserRouter>
      <App store={store} />
    </BrowserRouter>
  </StrictMode>,
  document.getElementById('root')
);
