import { StrictMode } from 'react';
import * as ReactDOM from 'react-dom';
import thunk from 'redux-thunk';
import { BrowserRouter } from 'react-router-dom';

import {
  signInSliceReducer,
  SIGNIN_USER_KEY,
} from '@client/market-app/sign-in';

import {
  SIGNUP_USER_KEY,
  signUpSliceReducer,
} from '@client/market-app/sign-ups';

import {
  registeredUserSliceReducer,
  REGISTERED_USER_KEY,
} from '@client/market-app/manage-users';

import App from './app/app';
import { configureStore } from '@reduxjs/toolkit';
import { CookiesProvider } from 'react-cookie';

const logger = (store) => (next) => (action) => {
  console.log('dispatching', action);
  const result = next(action);
  console.log('next state', store.getState());
  return result;
};

const store = configureStore({
  reducer: {
    [SIGNIN_USER_KEY]: signInSliceReducer,
    [SIGNUP_USER_KEY]: signUpSliceReducer,
    [REGISTERED_USER_KEY]: registeredUserSliceReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({ serializableCheck: false }).concat(logger),
});

ReactDOM.render(
  <StrictMode>
    <BrowserRouter>
      <CookiesProvider>
        <App store={store} />
      </CookiesProvider>
    </BrowserRouter>
  </StrictMode>,
  document.getElementById('root')
);
