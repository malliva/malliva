import { StrictMode } from 'react';
import * as ReactDOM from 'react-dom';
import thunk from 'redux-thunk';
import { BrowserRouter } from 'react-router-dom';

import {
  SIGNIN_USER_KEY,
  getSignInUserDetails,
} from '@client/market-app/sign-in';

import {
  SIGNUP_USER_KEY,
  signUpSliceReducer,
} from '@client/market-app/sign-ups';

import App from './app/app';
import { configureStore } from '@reduxjs/toolkit';

const logger = (store) => (next) => (action) => {
  console.log('dispatching', action);
  const result = next(action);
  console.log('next state', store.getState());
  return result;
};

const store = configureStore({
  reducer: {
    [SIGNIN_USER_KEY]: getSignInUserDetails,
    [SIGNUP_USER_KEY]: signUpSliceReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({ serializableCheck: false }).concat(logger),
});

ReactDOM.render(
  <StrictMode>
    <BrowserRouter>
      <App store={store} />
    </BrowserRouter>
  </StrictMode>,
  document.getElementById('root')
);
