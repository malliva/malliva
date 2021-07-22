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
  listUserSliceReducer,
  LIST_USER_KEY,
} from '@client/market-app/manage-users';

import {
  signOutUserSliceReducer,
  SIGNOUT_USER_KEY,
} from 'libs/market-app/sign-outs/src/index';

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
    [SIGNIN_USER_KEY]: signInSliceReducer,
    [SIGNUP_USER_KEY]: signUpSliceReducer,
    [LIST_USER_KEY]: listUserSliceReducer,
    [SIGNOUT_USER_KEY]: signOutUserSliceReducer,
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
