import { applyMiddleware, createStore } from 'redux';
import { persistStore } from 'redux-persist';
import rootReducer from './root-reducers';
import thunkMiddleware from 'redux-thunk';
import logger from 'redux-logger';
import { compose } from '@reduxjs/toolkit';

declare global {
  interface Window {
    __REDUX_DEVTOOLS_EXTENSION_COMPOSE__?: typeof compose;
  }
}
const composeEnhancers =
  (typeof window !== 'undefined' &&
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__) ||
  compose;

const middlewares = [logger, thunkMiddleware];

export const store = createStore(
  rootReducer,
  composeEnhancers(applyMiddleware(...middlewares))
);

export const persistor = persistStore(store);
