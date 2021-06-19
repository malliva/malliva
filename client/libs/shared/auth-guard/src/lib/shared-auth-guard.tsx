import React from 'react';
import { Redirect, Route } from 'react-router-dom';

import './shared-auth-guard.module.scss';

/* eslint-disable-next-line */
export interface SharedAuthGuardProps {}

export function SharedAuthGuard({ component: Component, auth, ...rest }) {
  return (
    <Route
      {...rest}
      render={(props) =>
        auth === true ? <Component {...props} /> : <Redirect to="/sign-in" />
      }
    />
  );
}

export default SharedAuthGuard;
