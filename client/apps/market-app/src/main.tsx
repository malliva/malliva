import { StrictMode } from 'react';
import * as ReactDOM from 'react-dom';
import thunk from 'redux-thunk';
import { BrowserRouter, useLocation, useParams } from 'react-router-dom';

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
import { combineReducers, configureStore } from '@reduxjs/toolkit';
import { Provider } from 'react-redux';

const logger = (store) => (next) => (action) => {
  console.log('dispatching', action);
  const result = next(action);
  console.log('next state', store.getState());
  return result;
};

const combinedReducer = combineReducers({
  [SIGNIN_USER_KEY]: signInSliceReducer,
  [SIGNUP_USER_KEY]: signUpSliceReducer,
  [LIST_USER_KEY]: listUserSliceReducer,
  [SIGNOUT_USER_KEY]: signOutUserSliceReducer,
});

const rootReducer = (state, action) => {
  if (action.type === 'malliva/logout/fulfilled') {
    state = undefined;
  }
  return combinedReducer(state, action);
};

const store = configureStore({
  reducer: rootReducer,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({ serializableCheck: false }).concat(logger),
});

ReactDOM.render(
  <StrictMode>
    <BrowserRouter>
      <Provider store={store}>
        <App />
      </Provider>
    </BrowserRouter>
  </StrictMode>,
  document.getElementById('root')
);
