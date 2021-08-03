import { applyMiddleware, createStore } from 'redux';
import { persistStore } from 'redux-persist';
import rootReducer from './root-reducers';
import thunkMiddleware from 'redux-thunk';

import logger from 'redux-logger';

const middlewares = [logger, thunkMiddleware];

export const store = createStore(rootReducer, applyMiddleware(...middlewares));

export const persistor = persistStore(store);
