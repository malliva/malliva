import { render } from '@testing-library/react';

import MarketAppManageUsers from './market-app-manage-users';

describe('MarketAppManageUsers', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<MarketAppManageUsers />);
    expect(baseElement).toBeTruthy();
  });
});
