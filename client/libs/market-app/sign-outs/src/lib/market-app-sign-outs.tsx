import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import {
  getCookieForUsers,
  postSingOutUser,
  setCookieForUsers,
} from '@client/shared/account-syn-api';

import './market-app-sign-outs.module.scss';
import {
  logout,
  selectSignOutStateStateLoaded,
} from './market-app-sign-outs.slice';

import { Link } from 'react-router-dom';

/* eslint-disable-next-line */
export interface MarketAppSignOutsProps {}

export function MarketAppSignOuts(props: MarketAppSignOutsProps) {
  const dispatch = useDispatch();
  const { loading } = useSelector(selectSignOutStateStateLoaded);

  useEffect(() => {
    if (loading === 'succeeded') {
      setCookieForUsers('create', 'jwt', '');
      dispatch(logout());
    }
  }, [dispatch, loading]);

  useEffect(() => {
    dispatch(postSingOutUser());
  }, [dispatch]);

  return (
    <div className="text-center">
      <h1>Welcome to market-app-sign-outs!</h1>
      <Link to="/sign-in">Sing in</Link>
    </div>
  );
}

export default MarketAppSignOuts;
